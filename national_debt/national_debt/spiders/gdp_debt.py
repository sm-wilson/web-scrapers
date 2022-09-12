import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        rows = response.xpath("//table[@class='jsx-364991517 table is-striped is-hoverable is-fullwidth tp-table-body is-narrow']/tbody/tr")
        for row in rows:
            yield {
                'Name': row.xpath('.//td[1]/a/text()').get(),
                'Debt Percent': row.xpath('.//td[2]/text()').get(),
                'Population': row.xpath('.//td[3]/text()').get()
            }
