import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']
    rules = ( Rule(LinkExtractor(), callback='parse_item', follow=True), )

    def parse_item(self, response):
        item = scrapy.Item()
        item['url'] = response.url
        self.logger.info('Hi, this is an item page! %s', response.url)
        return item

process = CrawlerProcess({ 'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' })
process.crawl(MySpider)
process.start()
