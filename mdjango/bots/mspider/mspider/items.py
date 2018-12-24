# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# from scrapy_djangoitem import DjangoItem
# from mova.models import Actor


# class FilmItem(DjangoItem):
#     DjangoItem = Actor


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    releasetime = scrapy.Field()
    type = scrapy.Field()
    ratestar = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    fweekbox = scrapy.Field()
    fdaybox = scrapy.Field()
    totalbox = scrapy.Field()
    score_910 = scrapy.Field()
    score_78 = scrapy.Field()
    score_56 = scrapy.Field()
    score_34 = scrapy.Field()
    score_12 = scrapy.Field()
    score_num = scrapy.Field()
