import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bizbuysell.com']
    start_urls = ['https://www.bizbuysell.com/online-and-technology-businesses-for-sale/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D']


    def parse(self, response):

        businessbox = response.css('a.diamond')

        tagline = businessbox.css('h3.title.ng-star-inserted::text').get()
        location = businessbox.css('p.location.ng-star-inserted::text').get().strip()
        askingprice = businessbox.css('p.asking-price.ng-star-inserted::text').get().strip()
        cashflow = businessbox.css('p.cash-flow.ng-star-inserted::text').get().replace('Cash Flow:','').strip()
        longdescription = businessbox.css('p.description.ng-star-inserted::text').get()
