import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bizbuysell.com']
    start_urls = [
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/2/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/3/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/4/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/5/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/6/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/7/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/8/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/9/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/10/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/11/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/12/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/13/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/14/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/15/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/16/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/17/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/18/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D',
        ]

    # 59 items on first page

    def parse(self, response):
        # page = 1
        businessbox = response.css('a.diamond')
        for business in businessbox:
            try:
                yield {
                    'Tag Line': business.css('h3.title.ng-star-inserted::text').get(),
                    'Location': business.css('p.location.ng-star-inserted::text').get(),
                    'Asking Price': business.css('p.asking-price.ng-star-inserted::text').get(),
                    'Cash Flow': business.css('p.cash-flow.ng-star-inserted::text').get(), #.replace('Cash Flow:', '').strip(),
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
        # page += 1
        # next_page = f'https://www.bizbuysell.com/online-and-technology-businesses-for-sale/{page}/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D'
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)