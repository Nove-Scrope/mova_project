# -*- coding: utf-8 -*-
import scrapy
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from  ..items import MovieItem
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from ..lilith import DataBase
import sqlite3

chrome_options = Options()
chrome_options.add_argument('--headless')
#try:
#    chrome_options.add_argument('executable_path = "./chromedriver"')
#except selenium.common.exceptions.WebDriverException:
#    chrome_options.add_argument('executable_path = "./chromedriver.exe"')
driver = webdriver.Chrome(chrome_options=chrome_options)
# DataBase.link('../mdjango/database.db')
dtb = DataBase()
dtb.link('D:\pyproject\mdjango\dtbase.db')
try:
    dtb.create_table()
except sqlite3.OperationalError:
    pass


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['piaofang.maoyan.com']
    start_urls = ['http://piaofang.maoyan.com/rankings/year']
    driver.get(start_urls[0])

    resultList = []
    # movie = {}

    def parse(self, response):
        fatherUrl = 'http://piaofang.maoyan.com'
        year_0 = 2019
        select_year = [2018, 2017, 2016, 2015]
        year_in = select_year[0]
        left_click = driver.find_element_by_xpath('//*[@id="tab-year"]/ul/li[' + str(year_0 - year_in) + ']')
        ActionChains(driver).move_to_element(left_click).perform()
        ActionChains(driver).double_click(left_click).perform()
        time.sleep(1)
        url_text = driver.page_source
        movie_herf = re.findall(r'data-com="hrefTo,href:\'(.*)\'\"', url_text)
        url_list = []
        # 这里修改需要爬取的条数
        for i in movie_herf[:10]:
            iurl = fatherUrl + i
            url_list.append(iurl)
            yield response.follow(iurl, callback=self.detail_parse)

    def detail_parse(self, response):
        movie = MovieItem()
        movie['name'] = response.xpath('//span[@class="info-title-content"]/text()').extract()[0]
        type = response.xpath('//p[@class="info-category"]/text()').extract()
        if type:
            type = type[0].split('\n')[1].strip()
        else:
            type = response.xpath('//span[@class="info-subtype ellipsis-1"]/text()').extract()
            if type:
                type = type[0]
            else:
                type = response.xpath('//span[@class="tv-types"]/text()').extract()[0]
        movie['type'] = type

        rlstime = response.xpath('//a/span[1]/text()').extract()
        if rlstime:
            movie['releasetime'] = rlstime[0]
        else:
            movie['releasetime'] = '--'
        # 星级评分
        star = response.xpath('//span[@class="rating-num"]/text()').extract()
        if star:
            movie['ratestar'] = star[0]
        else:
            movie['ratestar'] = '--'
        score_num = response.xpath('//p[@class="detail-score-count"]/text()').extract()
        # 评分人数
        if score_num:
            score_num = score_num[0].split("观众评分")[0]
            movie['score_num'] = score_num
            scoreflag = response.xpath('//div[@class="info-block"]/a/@href').extract()
            if scoreflag:
                # 猫眼各级评分人数占比
                score = response.xpath('//div[@class="percentbar"]/span/text()').extract()
                for i in range(0, 5):
                    label = 'score_' + str(9-2*i) + str(10-2*i)
                    movie[label] = score[2*i + 1]

        # 票房信息
        boxinfo = response.xpath('//div[@class="info-detail-row"]/div/p/span/text()').extract()
        if boxinfo:
            box = []
            for i in boxinfo:
                box.append(i)
                if i == '--':
                    box.append('--')
            cumbox = box[0] + box[1]
            if box[2] == '--':
                day1stbox = '--'
            else:
                day1stbox = box[2] + box[3]
            if box[4] == '--':
                week1stbox = '--'
            else:
                week1stbox = box[4] + box[5]
        else:
            cumbox = '--'
            day1stbox = '--'
            week1stbox = '--'
        movie['totalbox'] = cumbox
        movie['fdaybox'] = day1stbox
        movie['fweekbox'] = week1stbox
        actors_url = str(response).split(" ")[1].split(">")[0] + '/celebritylist'
        yield scrapy.Request(actors_url, meta={'movie': movie}, callback=self.director_parse)

    # 导演、演员信息
    def director_parse(self, response):
        movie = response.meta['movie']
        person_detail = response.xpath('//div[@class="panel-wrapper"]//span[@class="title-name"]/text()').extract()
        findlabel = ['导演', '演员']
        if findlabel[0] in person_detail:
            dposition = person_detail.index(findlabel[0]) + 1
        else:
            dposition = -1
        if findlabel[1] in person_detail:
            aposition = person_detail.index(findlabel[1]) + 1
        else:
            aposition = -1
        if dposition == -1:
            director = '--'
        else:
            director = response.xpath('//div[@class="panel-wrapper"]/dl['+str(dposition)+']//div[@class="p-desc"]'
                                                                                         '/p[1]/text()').extract()
            if director:
                pass
            else:
                director = response.xpath('//div[@class="p-desc"]/p[' + str(dposition) + ']/text()').extract()
        movie['director'] = director

        if aposition == -1:
            actor = '--'
        else:
            actor = response.xpath('//div[@class="panel-wrapper"]/dl[' + str(aposition) + ']//div/p[1]/text()').extract()
        actorlen  = 10
        if len(actor) <= actorlen:
            movie['actor'] = actor
        else:
            movie['actor'] = actor[:actorlen]
        # yield movie
        self.resultList.append(movie)

    def close(self, reason):
        for i in self.resultList:
            print(i)
            filmInfo = {}
            filmInfo['date'] = i['releasetime']
            filmInfo['boxoffice'] = i['totalbox']
            filmInfo['score'] = i['ratestar']
            filmInfo['name'] = i['name']
            filmInfo['type'] = i['type']
            dtb.film_in(filmInfo)
            actorInfo = i['actor']
            for j in actorInfo:
                dtb.actor_in({'name': j}, filmInfo['name'])
            directorInfo = i['director']
            for j in directorInfo:
                dtb.director_in({'name': j}, filmInfo['name'])
