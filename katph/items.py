# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class AppItem(scrapy.Item):
    # define the fields for your item here like:
    app_title = scrapy.Field()
    app_name = scrapy.Field()
    category = scrapy.Field()
    appstore_link = scrapy.Field()
    img_src = scrapy.Field()


class StackItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

class DribbleItem(scrapy.Item):
    title = scrapy.Field()
    thumbnail = scrapy.Field()
    views = scrapy.Field()
    comments = scrapy.Field()
    favs = scrapy.Field()

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class ItuneApp(scrapy.Item):
    guid = scrapy.Field()

    NameOfApplication = scrapy.Field()

    Itunes_Link = scrapy.Field()
    thumbnail = scrapy.Field()

    LastTimeUpdatedDate = scrapy.Field()

    Developer = scrapy.Field()
    Website = scrapy.Field()

    ofReviews = scrapy.Field()
    ofReviewsCurrent = scrapy.Field()

    starts = scrapy.Field()
    startsCurrent = scrapy.Field()

    version = scrapy.Field()
    # description = scrapy.Field()


class KatPHItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class StackItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()


class KatphItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TripItem(scrapy.Item):
    route_name = scrapy.Field()
    origin_name = scrapy.Field()
    destination_name = scrapy.Field()
    departure_time = scrapy.Field()
    arrival_time = scrapy.Field()
    duration = scrapy.Field()
    price = scrapy.Field()
