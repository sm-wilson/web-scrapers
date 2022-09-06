from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BizbuySpider(CrawlSpider):
    name = 'bizbuy'
    allowed_domains = ['bizbuysell.com']
    start_urls = [
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D']

    rules = [
        Rule(
            LinkExtractor(
                restrict_text=()
            )
        )
    ]

    def parse_business(self, response):
        pass
