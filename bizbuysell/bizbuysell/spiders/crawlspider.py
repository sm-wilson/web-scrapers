import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = 'crawlspider'
    allowed_domains = ['bizbuysell.com']
    start_urls = ['https://www.bizbuysell.com/online-and-technology-businesses-for-sale/1/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D']
    rules = (
        Rule(LinkExtractor(allow='Business-Opportunity'), callback='parse_biz'),
    )


    def parse_biz(self, response):
        yield {
            'title': response.css('h1.bfsTitle::text').get().strip(),
            'location': response.css('h2.gray::text').get().strip(),
            'askingprice': response.css('p.help b::text')[0].get().strip(),
            'cashflow': response.css('p.help b::text')[1].get().strip(),
            'grossrevenue': response.css('p.help b::text')[2].get().strip(),
            'EBITDA': response.css('p.help b::text')[3].get().strip(),
            'FF&E': response.css('p.help b::text')[4].get().strip(),
            'inventory': response.css('p.help b::text')[5].get().strip(),
            'year_estd': response.css('p.odd b::text')[3].get()
        }
