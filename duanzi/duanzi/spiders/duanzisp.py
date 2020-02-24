# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from duanzi.items import DuanziItem
import re

class DuanzispSpider(scrapy.Spider):
    name = 'duanzisp'
    allowed_domains = ['duanziwang.com']
    start_urls = ['https://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/1/']

    def parse(self, response):
        articles = response.xpath('//article')
        next = response.xpath('//nav/a[@class="next"]')
        for article in articles:
            title = article.xpath('.//div/h1/a/text()').get().split('_')[0]
            content = article.xpath('.//div/p/text()').get()
            item = DuanziItem(title=title, content=content)
            yield item
        if next:
            selfre = re.compile('90/(\d+)/')
            selfno = re.search(selfre, response.url).group(1)
            print('selfno', selfno)
            nexturl = re.sub(selfre, '90/'+str(int(selfno)+1)+'/', response.url)
            print('nexturl', nexturl)
            yield scrapy.Request(url=nexturl, callback=self.parse)
        else:
            return






















pass
