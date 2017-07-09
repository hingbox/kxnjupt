# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#用来对爬出来的item进行后续处理，入存入数据库等
import json
import codecs
class NjuptPipeline(object):
    def __init__(self):
        self.file = open('D:\\PycharmProjects\\njupt\\njupt.txt', mode='wb')
    def process_item(self, item, spider):
        self.file.write(item['news_title'].encode("GBK"))
        self.file.write("\n")
        self.file.write(item['news_date'].encode("GBK"))
        self.file.write("\n")
        self.file.write(item['news_url'].encode("GBK"))
        self.file.write("\n")
        return item

class TestPlipeline(object):
    def __init__(self):
        self.file = codecs.open('D:\\PycharmProjects\\data.json', mode='wb', encoding='utf-8')  # 数据存储到data.json

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))
        return item