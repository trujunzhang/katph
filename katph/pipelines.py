# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

from datetime import datetime
from hashlib import md5

class MongoPipeline(object):
    collection_name = 'katph_itunes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_SERVER'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        guid = self._get_guid(item)

        item["guid"] = guid
        item["updatedAt"] = datetime.utcnow().replace(microsecond=0).isoformat(' ')

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid:
            cursor = self.db[self.collection_name].find({'guid':guid})
            if cursor.count():
                valid = False
                raise DropItem("Duplicate item found: {0}!".format(data))
        if valid:
            self.db[self.collection_name].insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

    def _get_guid(self, item):
        """Generates an unique identifier for a given item."""
        # hash based solely in the url field
        return md5(item['name']).hexdigest()