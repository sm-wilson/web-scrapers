item name
products = response.css('div.item-container')
products.css('a.item-title::text').get()

price
price = products.css('div.item-action')
dollars
price.css('strong')
products.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price-current", " " ))]//strong/text()').get()
products.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price-current", " " ))]//strong/text()').get()
cents
price.css('sup')
products.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price-current", " " ))]//sup/text()').get()


products.xpath("//div[@class='item-action']//ul//li[@class='price-current']//strong/text()").get()
products.xpath("//div[@class='item-action']//ul//li[@class='price-current']//sup/text()").get()
