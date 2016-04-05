# scrapy crawl dmoz -o items.json -t json
# scrapy crawl dmoz

import scrapy

from scrapy.selector import Selector

from katph.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org"
    ]
    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]


    # rules = [Rule(SgmlLinkExtractor(), callback='parse_item', follow=True)]

    def parsexx(self,response):
        self.log('A response from %s just arrived!' % response.url)

    def parse(self,response):
        response_url = response.url
        self= Selector(response)
        sites = self.xpath('//ul/li')
        items = []
        for site in sites:
           item = DmozItem()
           item['title'] = site.xpath('a/text()').extract()
           item['link'] = site.xpath('a/@href').extract()
           item['desc'] = site.xpath('text()').extract()
           items.append(item)
        return items

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     open(filename,'wb').write(response.body)

