# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

#这个类是用来存储趴下来的数据结构(字典形式)
class NjuptItem(Item):#NjuptItem 为自动生成的类名
    new_title = Field()#新闻title
    new_date = Field()#新闻日期
    new_url = Field()#新闻链接


class TestItem(Item):
    title = Field()
    author = Field()
    view = Field()
    releasedate = Field()
