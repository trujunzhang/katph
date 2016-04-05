# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from katph.items import StackItem


class StackSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'http://stackoverflow.com/questions?pagesize=50&sort=newest'
    ]

    rules = [
        Rule(LinkExtractor(allow=r'questions\?page=[0-9]&sort=newest'),
             callback='parse_item', follow=True)
    ]

    # def parse(self, response):
    #     url = response.url
    #
    #     return url

    def parse_item(self, response):
        item = StackItem()
        item['url'] = response.url

        return item

    def parse_itemxxx(self, response):
        if len(self.start_urls) == 1:
            self.start_urls.append("http://www.baidu.com")
            self.rules.append(LinkExtractor(allow=r'questions\?page=[0-9]&sort=newest'),
                              callback='parse_item', follow=True)

        if "baidu" in response.url:
            url = response.url

        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            yield item
