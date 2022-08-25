import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bizbuysell.com']
    start_urls = [
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D']

    # 59 items on first page

    def parse(self, response):

        businessbox = response.css('a.diamond')
        for business in businessbox:
            try:
                yield {
                    'tagline': business.css('h3.title.ng-star-inserted::text').get(),
                    'location': business.css('p.location.ng-star-inserted::text').get().strip(),
                    'askingprice': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                    'cashflow': business.css('p.cash-flow.ng-star-inserted::text').get().replace('Cash Flow:', '').strip(),
                    'longdescription': business.css('p.description.ng-star-inserted::text').get()
                }
            except AttributeError:
                if business.css('p.cash-flow.ng-star-inserted::text').get() is None:
                    yield {
                        'tagline': business.css('h3.title.ng-star-inserted::text').get(),
                        'location': business.css('p.location.ng-star-inserted::text').get().strip(),
                        'askingprice': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'cashflow': 'n/a',
                        'longdescription': business.css('p.description.ng-star-inserted::text').get()
                    }
                elif business.css('p.location.ng-star-inserted::text').get() is None:
                    yield {
                        'tagline': business.css('h3.title.ng-star-inserted::text').get(),
                        'location': 'n/a',
                        'askingprice': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'cashflow': business.css('p.cash-flow.ng-star-inserted::text').get().replace('Cash Flow:', '').strip(),
                        'longdescription': business.css('p.description.ng-star-inserted::text').get()
                    }
                elif business.css('p.location.ng-star-inserted::text').get() is None and business.css('p.cash-flow.ng-star-inserted::text').get() is None:
                    yield {
                        'tagline': business.css('h3.title.ng-star-inserted::text').get(),
                        'location': 'n/a',
                        'askingprice': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'cashflow': 'n/a',
                        'longdescription': business.css('p.description.ng-star-inserted::text').get()
                    }
