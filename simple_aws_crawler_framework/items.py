# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SimpleAwsCrawlerFrameworkItem(scrapy.Item):
    # define the fields for your item here like:
    header = scrapy.Field()
    url = scrapy.Field()
    pass


class CrawlingPaginationItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    summary = scrapy.Field()
    pass


class Post(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    pass


# class History(scrapy.Item):
#     # define the fields for your item here like:
#     keyword = scrapy.Field()
#     date = scrapy.Field()
#     pass
