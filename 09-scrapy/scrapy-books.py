# url https://books.toscrape.com/

import scrapy


class BookSpider(scrapy.Spider):
    name = 'booksspider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css('.price_color::text').extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first()
            }
            # on the page there is a button next inside 'li' with class 'next'
            next = response.css('.next > a::attr(href)').extract_first()
            # if there is 'next' button then follow it and scrape the page recursively
            if next:
                yield response.follow(next, self.parse)
