import scrapy


class ImomoeSpider(scrapy.Spider):
    name = 'imomoe'
    allowed_domains = ['imomoe.in']
    start_urls = ['http://www.imomoe.in/view/7883.html']

    def parse(self, response):
        # for url in response.xpath("descendant-or-self::*[@id = 'play_0']/ul/li/a/@href").extract():
        for href in response.css("#play_0 > ul > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents())

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
