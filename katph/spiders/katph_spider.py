import scrapy
from scrapy.selector import Selector

from katph.items import KatPHItem


class katphSpider(scrapy.Spider):
    name = "katph"
    allowed_domains = ["kat.cr"]
    start_urls = [
        "https://kat.cr/usearch/java/"
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        self = Selector(response)
        sites = self.xpath('//tr/td/div[@class="torrentname"]/div[@class="markeredBlock torType zipType"]')
        items = []
        for site in sites:
            item = KatPHItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items

    def parse_itemxx(self, response):
        response_url = response.url
        self = Selector(response)
        sites = self.xpath('//ul/li')
        items = []
        for site in sites:
            item = KatPHItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items
