# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookmyshowItem(scrapy.Item):
    
    show_links= scrapy.Field()

class BookmyshowMovieItems(scrapy.Item):
	movie_genre=scrapy.Field()
	movie_userrating=scrapy.Field()
	movie_criticsrating=scrapy.Field()
	movie_lang=scrapy.Field()
	movie_name=scrapy.Field()
	movie_time=scrapy.Field()
	movie_percent=scrapy.Field()
	movie_link=scrapy.Field()