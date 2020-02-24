# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
import json

# 这种方法是用 原始的 将数据转成json
class DuanziPipeline(object):


    # 在初始化方法中打开duanzi.json
    def __init__(self):
        self.fp = open('duanzi.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')

    # 在这个方法中 将 数据 写入 json 文件中
    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了')
'''

from scrapy.exporters import JsonLinesItemExporter


# 这种方法是用 scrapy 框架自带的导出json数据,但是怎么感觉这样写反而麻烦呢
class DuanziPipeline(object):

    # 在初始化方法中打开duanzi.json
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')

    # 在这个方法中 将 数据 写入 json 文件中
    def process_item(self, item, spider):
        # 这里简单了，不用转格式什么的了
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了')

    pass
