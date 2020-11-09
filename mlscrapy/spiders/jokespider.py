# -*- coding: utf-8 -*-
import scrapy
from jokeItem import JokeItem
from scrapy.loader import ItemLoader

class JokespiderSpider(scrapy.Spider):
    name = 'jokespider'
    allowed_domains = ['www.laughfactory.com']
    start_urls = ['https://www.laughfactory.com/jokes/family-jokes']

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            l= ItemLoader(item=JokeItem(), selector=joke)
            l.add_xpath('joke_text', ".//div[@class='joke-text']/p")
            yield l.load_item()
        
        next_page= response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)  


             
    
