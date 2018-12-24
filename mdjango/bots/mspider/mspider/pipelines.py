# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# from mova.models import Actor, Film, Type, Director


class MspiderPipeline(object):
    def process_item(self, item, maoyan):
        # item.save()
        return item

# import os
# import csv
#
#
# class MspiderPipeline(object):
#
#     def __init__(self):
#         store_file = os.path.dirname(__file__) + 'spiders/qtw.csv'
#         self.file = open(store_file, 'wb')
#         self.writer = csv.writer(self.file)
#
#     def process_item(self, item, spider):
#         if item['actor']:
#             self.writer.writerow(item['actor'].encode('utf8', 'ignore'))
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()
