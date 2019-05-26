# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.conf import settings
import pymongo


class LianjiaPipeline(object):
    def __init__(self):
        self.host = settings["MONGODB_HOST"]
        self.port = settings["MONGODB_PORT"]
        self.dbname = settings["MONGODB_DBNAME"]
        self.sheetname = settings["MONGODB_SHEETNAME"]


    def open_spider(self,spider):
        # 创建MONGODB数据库链接
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        # 指定数据库
        self.mydb = self.client[self.dbname]
        # 存放数据的数据库表名
        self.post = self.mydb[self.sheetname]

    def process_item(self,item,spider):
        self.post.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()