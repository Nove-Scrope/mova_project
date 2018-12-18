#from scrapy import cmdline
# 执行
# cmdline.execute('scrapy crawl maoyan'.split())
# 写入csv文件
# cmdline.execute('scrapy crawl maoyan -o result.csv'.split())
def run_spider():
#	print("5")
	from scrapy.crawler import CrawlerProcess
	from bots.mspider.mspider.spiders.maoyan import DoubanSpider
	process = CrawlerProcess({
		'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
					  '537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
	})
	process.crawl(DoubanSpider)
	process.start()
