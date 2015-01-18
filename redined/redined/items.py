# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc__scrapy__org/en/latest/topics/items__html

import scrapy


class RedinedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    DCTERMS__extent = scrapy.Field()
    DCTERMS__abstract = scrapy.Field()
    citation_date = scrapy.Field()
    citation_pdf_url = scrapy.Field()
    DCTERMS__dateAccepted = scrapy.Field()
    DC__language = scrapy.Field()
    DC__title = scrapy.Field()
    DC__type = scrapy.Field()
    DC__date = scrapy.Field()
    DC__creator = scrapy.Field()
    DCTERMS__issued = scrapy.Field()
    citation_language = scrapy.Field()
    citation_keywords = scrapy.Field()
    citation_title = scrapy.Field()
    DC__description = scrapy.Field()
    citation_authors = scrapy.Field()
    citation_abstract_html_url = scrapy.Field()
    DCTERMS__medium = scrapy.Field()
    DC__identifier = scrapy.Field()
    DC__contributor = scrapy.Field()
    DC__relation = scrapy.Field()
    DCTERMS__available = scrapy.Field()
    DC__subject = scrapy.Field()
    centro_ed = scrapy.Field()
    audiencia = scrapy.Field()
    nivel = scrapy.Field()
    tipo = scrapy.Field()
    #nivel = scrapy.Field()
    #nivel = scrapy.Field()