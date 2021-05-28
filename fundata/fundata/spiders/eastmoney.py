import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/fund.html']

    def parse(self, response):
        pass
