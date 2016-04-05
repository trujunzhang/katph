from scrapy.contrib.spiders import CrawlSpider
from katph.items import DribbleItem
from scrapy.selector import Selector

class ShoeSpider(CrawlSpider):
    name = 'dribbble'
    allowed_domains = ['localhost.com']
    start_urls = ['http://localhost:8888/Download/dribble.html']

    def parse(self, response):
        select = '//li[@class="group"]'
        sel = Selector(response)
        groups = sel.xpath(select)

        count = 0
        items = []
        for app in groups:
            item = DribbleItem()
            item['app_title'] = type
            item['app_name'] = app.xpath('//h3/a/text()')[count].extract()
            item['appstore_link'] = app.xpath('//h3/a/@href')[count].extract()
            item['category'] = app.xpath('//h4/a/text()')[count].extract()
            item['img_src'] = app.xpath('//a/img/@src')[count].extract()
            items.append(item)
            count += 1

        return items