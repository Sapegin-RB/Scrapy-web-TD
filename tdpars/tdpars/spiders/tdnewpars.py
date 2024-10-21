import scrapy


class TdnewparsSpider(scrapy.Spider):
    name = "tdnewpars"
    allowed_domains = ["https://tdom.info"]
    start_urls = ["https://tdom.info/santehnika/polotencesushiteli-i-komplektuyuschie"]

    def parse(self, response):
        pass
