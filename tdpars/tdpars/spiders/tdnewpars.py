import scrapy

class TdnewparsSpider(scrapy.Spider):
    name = "tdnewpars"
    allowed_domains = ["tdom.info"]
    start_urls = ["https://tdom.info/santehnika/polotencesushiteli-i-komplektuyuschie"]

    def parse(self, response):
        towels = response.css("div.product-thumb")
        for towel in towels:
            name = towel.css("span.item-name::text").get()
            price = towel.css("p.price::text").get()
            url = towel.css("div.caption a").attrib["href"]

            # Проверяем, что name не None перед вызовом .strip()
            yield {
                "name": name.strip() if name else "Название отсутствует",
                "price": price.strip() if price else "Цена отсутствует",
                "url": url if url else "URL отсутствует"
            }
