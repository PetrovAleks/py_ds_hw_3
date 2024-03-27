from scrapy.crawler import CrawlerProcess
from py_ds_hw_3.spider.spider import MySpider

def init():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    print("py_ds_hw_3 is initialized")
    process.crawl(MySpider)
    process.start()