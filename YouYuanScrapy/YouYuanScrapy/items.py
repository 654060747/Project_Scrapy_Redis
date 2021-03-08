# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YouyuanscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    net_name = scrapy.Field()
    city = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    salary = scrapy.Field()
    house = scrapy.Field()
    weight = scrapy.Field()
    education = scrapy.Field()
    marriage = scrapy.Field()
    img_url = scrapy.Field()
    pass
