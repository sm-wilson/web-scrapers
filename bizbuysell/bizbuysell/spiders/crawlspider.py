from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = 'crawlspider'
    allowed_domains = ['bizbuysell.com']
    start_urls = ['https://www.bizbuysell.com/online-and-technology-businesses-for-sale/18/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D']
    rules = (
        Rule(LinkExtractor(allow='Business-Opportunity'), callback='parse_biz'),
    )


    def parse_biz(self, response):
        try:
            yield {
                'Link': response.request.url,
                'Title': response.xpath("//h1[@class='bfsTitle']/text()").get(),
                'Location': response.xpath("//h2[@class='gray']/text()").get(),
                'Asking Price': response.xpath("//p[@class='price asking help  odd']/b/text()").get(),
                'Cash Flow': response.xpath("//p[@class='price help  ']/b/text()").get(),
                'Gross Revenue': response.xpath("//p[@class='help  odd']/b/text()").get(),
                'EBITDA': response.xpath("//p[@class='notDisclosed help  ']/b/text()").get(),
                'FF&E': response.xpath("//p[@class='help  odd'][2]/b/text()").get(),
                'Inventory': response.xpath("//p[@class='help niiap ']/b/text()").get(),
            }
        except AttributeError:
            if response.xpath("//p[@class='price help  ']/b/text()").get() is None: # Cash Flow is empty
                yield {
                    'Link': response.request.url,
                    'Title': response.xpath("//h1[@class='bfsTitle']/text()").get(),
                    'Location': response.xpath("//h2[@class='gray']/text()").get(),
                    'Asking Price': response.xpath("//p[@class='price asking help  odd']/b/text()").get(),
                    'Cash Flow': 'N/A',
                    'Gross Revenue': response.xpath("//p[@class='help  odd']/b/text()").get(),
                    'EBITDA': response.xpath("//p[@class='notDisclosed help  ']/b/text()").get(),
                    'FF&E': response.xpath("//p[@class='help  odd'][2]/b/text()").get(),
                    'Inventory': response.xpath("//p[@class='help niiap ']/b/text()").get(),
                }
            if response.xpath("//p[@class='help niiap ']/b/text()").get() is None: # Inventory is empty
                yield {
                    'Link': response.request.url,
                    'Title': response.xpath("//h1[@class='bfsTitle']/text()").get(),
                    'Location': response.xpath("//h2[@class='gray']/text()").get(),
                    'Asking Price': response.xpath("//p[@class='price asking help  odd']/b/text()").get(),
                    'Cash Flow': response.xpath("//p[@class='price help  ']/b/text()").get(),
                    'Gross Revenue': response.xpath("//p[@class='help  odd']/b/text()").get(),
                    'EBITDA': response.xpath("//p[@class='notDisclosed help  ']/b/text()").get(),
                    'FF&E': response.xpath("//p[@class='help  odd'][2]/b/text()").get(),
                    'Inventory': 'N/A',
                }
            if response.xpath("//p[@class='notDisclosed help  ']/b/text()").get() is None: # EBITDA is empty
                yield {
                    'Link': response.request.url,
                    'Title': response.xpath("//h1[@class='bfsTitle']/text()").get(),
                    'Location': response.xpath("//h2[@class='gray']/text()").get(),
                    'Asking Price': response.xpath("//p[@class='price asking help  odd']/b/text()").get(),
                    'Cash Flow': response.xpath("//p[@class='price help  ']/b/text()").get(),
                    'Gross Revenue': response.xpath("//p[@class='help  odd']/b/text()").get(),
                    'EBITDA': 'N/A',
                    'FF&E': response.xpath("//p[@class='help  odd'][2]/b/text()").get(),
                    'Inventory': response.xpath("//p[@class='help niiap ']/b/text()").get(),
                }
