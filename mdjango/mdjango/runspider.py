# coding:utf-8
import threading
# 在项目外用脚本启动爬虫
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings


def run_csbk():
    settings = Settings({
        'SPIDER_MODULES': ['bots.mspider.mspider.spiders.maoyan'],
        'ROBOTSTXT_OBEY': False,
        # 设置包头
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'http://piaofang.maoyan.com/rankings/year',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'},
        # 启用pipelines组件
        # 'ITEM_PIPELINES': {
        #     'mspider.mspider.spiders.MspiderPipeline': 400, },
        'ITEM_PIPELINES': {
            'bots.mspider.mspider.pipelines.MspiderPipeline': 100,},
        'CONCURRENT_REQUESTS': 1,  # 同时只处理一个请求
        'DOWNLOAD_DELAY': 1  # 每个1秒 下载一个页面
    })
    runner = CrawlerRunner(settings)
    d = runner.crawl('maoyan')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return 0


def thread(signal):
    if signal:
        threading.Thread(target=run_csbk())
    else:
        return 0
