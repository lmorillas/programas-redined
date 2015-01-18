# -*- coding: utf-8 -*-
import scrapy
import urlparse
from redined.items import RedinedItem

BASE = 'http://redined.mecd.gob.es/'
BASEp = 'http://redined.mecd.gob.es/xmlui/'

class AragonSpider(scrapy.Spider):
    name = "aragon"
    allowed_domains = ["redined.mecd.gob.es"]
    start_urls = (
        #'http://redined.mecd.gob.es/xmlui/discover?scopeFilter=Innovaciones&query=arag%C3%B3n&submit=Ir',
        'http://redined.mecd.gob.es/xmlui/discover?scopeFilter=Innovaciones&query=%22Gobierno+de+Arag%C3%B3n%22+%22Pol%C3%ADtica+Educativa%22&submit=Ir&scopeFilter=',

    )

    def parse(self, response):
        siguientes = response.selector.xpath(u'//a[@class="next-page-link"]/@href').extract()
        if siguientes:
            yield scrapy.Request(urlparse.urljoin(BASEp, siguientes[0]))
        for link in response.selector.xpath(u'//div[@class="artifact-title"]/a/@href').extract():
            yield scrapy.Request(urlparse.urljoin(BASE, link +'?show=full'), callback=self.parse_item)

    def parse_item(self, response):
        def mangle(x):
            return x.replace('.', '__')
        claves = [u'DCTERMS.extent', u'DCTERMS.abstract', u'citation_date',
        u'citation_pdf_url', u'DCTERMS.dateAccepted', u'DC.language', u'DC.title', u'DC.type',
        u'DC.date', u'DC.creator', u'DCTERMS.issued', u'citation_language', u'citation_keywords',
        u'citation_title', u'DC.description', u'citation_authors', u'citation_abstract_html_url',
        u'DCTERMS.medium', u'DC.identifier', u'DC.contributor', u'DC.relation', u'DCTERMS.available',
        u'DC.subject']

        exprxp = '//meta[@name="{}"]/@content'
        exprxptabla = '//td[text() = "{}"]/following-sibling::td[1]/text()'
        item = RedinedItem()
        sel = response.selector

        for k in claves:
            item[mangle(k)] = sel.xpath(exprxp.format(k)).extract()
            item['centro_ed'] = sel.xpath(exprxptabla.format("dc.contributor.other")).extract()
            item['audiencia'] = sel.xpath(exprxptabla.format("dc.audience")).extract()
            item['nivel'] = sel.xpath(exprxptabla.format('dc.educationLevel')).extract()
            item['tipo'] = sel.xpath(exprxptabla.format('dc.type')).extract()


        yield item

