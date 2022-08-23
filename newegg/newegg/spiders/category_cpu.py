import scrapy


class CategoryCpuSpider(scrapy.Spider):
    name = 'category_cpu'
    allowed_domains = ['newegg.com']
    start_urls = [
        'https://www.newegg.com/Processors-Desktops/SubCategory/ID-343?Tid=7671']

    def parse(self, response):
        # item name
        products = response.css('div.item-container')
        prices = products.css('div.item-action')
        # item = {'name': [], 'price': [], 'promo': []}
        for product in products[1:]:
            
            yield {
                'name': product.css('a.item-title::text').get(),
                'price': product.xpath("//div[@class='item-action']//ul//li[@class='price-current']//strong/text()").get()
                + product.xpath("//div[@class='item-action']//ul//li[@class='price-current']//sup/text()").get(),

                'link': product.css('a.item-title::attr(href)').get(),
                'promo': product.css('p.item-promo::text').get()
            }
