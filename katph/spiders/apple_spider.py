import scrapy

from katph.items import AppItem
from scrapy.selector import Selector


class AppleSpider(scrapy.Spider):
    name = "apple"
    allowed_domains = ["apple.com"]
    start_urls = ["http://www.apple.com/itunes/charts"]

    allowed_nav_titles = ["Free Apps", "Paid Apps"]

    domain = "http://www.apple.com"

    def allowNav(self, title):
        for allowed_title in self.allowed_nav_titles:
            if allowed_title == title:
                return True
        return False

    def getAbstractPath(self, domain, path):
        return ('%s%s' % domain % path)

    def parse(self, response):
        select = '//div[@class="subnav"]/a'
        sel = Selector(response)
        navs = sel.xpath(select)
        count = 0
        for nav in navs:
            title = nav.xpath('//div[@class="subnav"]/a/text()')[count].extract()
            path = nav.xpath('//div[@class="subnav"]/a/@href')[count].extract()
            count += 1
            if self.allowNav(title):
                abstractPath = (self.domain + path)
                yield scrapy.Request(abstractPath, self.parse_details, meta={'type': title})

    def parse_details(self, response):
        response_url = response.url
        type = response.meta['type']
        sel = Selector(response)
        apps = sel.xpath('//div[@class="section-content"]/ul/li')
        count = 0
        items = []
        for app in apps:
            item = AppItem()
            item['app_title'] = type
            item['app_name'] = app.xpath('//h3/a/text()')[count].extract()
            item['appstore_link'] = app.xpath('//h3/a/@href')[count].extract()
            item['category'] = app.xpath('//h4/a/text()')[count].extract()
            item['img_src'] = app.xpath('//a/img/@src')[count].extract()
            items.append(item)
            count += 1
        return items
