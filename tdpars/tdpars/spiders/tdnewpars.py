import scrapy


class TdnewparsSpider(scrapy.Spider):
    name = "tdnewpars"
    allowed_domains = ["https://tdom.info"]
    start_urls = ["https://tdom.info/santehnika/polotencesushiteli-i-komplektuyuschie"]

    def parse(self, response):
        towels = response.css("span.item-name")
        for towel in towels:
            yield {
                "name" : towel.css("div.caption span.item-name").get(),
                "price" : towel.css("div.option span.item-name").get(),
                "url" : towel.css("a").attrib["href"]
            }


