# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import  TakeFirst
from scrapy.loader import ItemLoader

class FirstItemLoader(ItemLoader):
    #自定义itemloader，继承scrapy的ItemLoader类
    default_output_processor = TakeFirst()

class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    id = scrapy.Field()
    quyu = scrapy.Field()
    shangquan = scrapy.Field()
    xiaoqu = scrapy.Field()
    priceTotal = scrapy.Field()
    pricePerSqm = scrapy.Field()
    huxing = scrapy.Field()
    sqmTotal = scrapy.Field()
    sqmInner = scrapy.Field()
    chaoxiang = scrapy.Field()
    zhuangxiu = scrapy.Field()
    elevator = scrapy.Field()
    floor = scrapy.Field()
    hxStructure = scrapy.Field()
    leixing = scrapy.Field()
    jzStructure = scrapy.Field()
    elevatorRatio = scrapy.Field()
    nianxian = scrapy.Field()
    onlineDate = scrapy.Field()
    lastTradeDate = scrapy.Field()
    houseYear = scrapy.Field()
    diya = scrapy.Field()
    quanshu = scrapy.Field()
    yongtu = scrapy.Field()
    chanquan = scrapy.Field()
    pass
