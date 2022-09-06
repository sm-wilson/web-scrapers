import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bizbuysell.com']
    start_urls = [
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/4/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D'
        ]

    # 59 items on first page

    def parse(self, response):
        businessbox = response.css('a.diamond')
        for business in businessbox:
            try:
                yield {
                    'Tag Line': business.css('h3.title.ng-star-inserted::text').get(),
                    'Location': business.css('p.location.ng-star-inserted::text').get(),
                    'Asking Price': business.css('p.asking-price.ng-star-inserted::text').get(),
                    # .replace('Cash Flow:', '').strip(),
                    'Cash Flow': business.css('p.cash-flow.ng-star-inserted::text').get().replace('Cash Flow:', ''),
                    'Long Description': business.css('p.description.ng-star-inserted::text').get()
                }
            except AttributeError:
                if business.css('p.cash-flow.ng-star-inserted::text').get() is None:
                    yield {
                        'Tag Line': business.css('h3.title.ng-star-inserted::text').get(),
                        'Location': business.css('p.location.ng-star-inserted::text').get().strip(),
                        'Asking Price': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'Cash Flow': 'n/a',
                        'Long Description': business.css('p.description.ng-star-inserted::text').get()
                    }
                elif business.css('p.location.ng-star-inserted::text').get() is None:
                    yield {
                        'Tag Line': business.css('h3.title.ng-star-inserted::text').get(),
                        'Location': 'n/a',
                        'Asking Price': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'Cash Flow': business.css('p.cash-flow.ng-star-inserted::text').get().replace('Cash Flow:', '').strip(),
                        'Long Description': business.css('p.description.ng-star-inserted::text').get()
                    }
                elif business.css('p.location.ng-star-inserted::text').get() is None and business.css('p.cash-flow.ng-star-inserted::text').get() is None:
                    yield {
                        'Tag Line': business.css('h3.title.ng-star-inserted::text').get(),
                        'Location': 'n/a',
                        'Asking Price': business.css('p.asking-price.ng-star-inserted::text').get().strip(),
                        'Cash Flow': 'n/a',
                        'Long Description': business.css('p.description.ng-star-inserted::text').get()
                    }
        # page_list = ['https://www.bizbuysell.com/online-and-technology-businesses-for-sale/'+ str(i)+'/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D' for i in range(1, 18)]
        
        # # next_page = f'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/{page}/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D'
        # for page in page_list:
        #     if page is not None:
        #         yield response.follow(page, callback=self.parse)
