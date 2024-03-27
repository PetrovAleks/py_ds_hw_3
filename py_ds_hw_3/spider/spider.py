import scrapy
from scrapy.selector import SelectorList
from scrapy.http import Response
from scrapy.http import Response
from py_ds_hw_3.items import AuthorItem, QuoteItem


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://quotes.toscrape.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'py_ds_hw_3.pipelines.AuthorJsonWriterPipeline': 300,
            'py_ds_hw_3.pipelines.QuoteJsonWriterPipeline': 400,
        },
        'AUTOTHROTTLE_ENABLED':True
    }

    def set_author(self, response:SelectorList):
        author = AuthorItem()
        author["fullname"] = response.css('.author-title::text').get()
        author["born_date"] = response.css('.author-born-date::text').get()
        author["born_location"] = response.css('.author-born-location::text').get()
        author["description"] = response.css('.author-description::text').get()
        yield author
        
    def set_quote(self, response:SelectorList):
        quote_item = QuoteItem()  
        quote_item["quote"] = response.css('.text::text').get()
        quote_item["tags"] = response.css('.tag::text').getall()
        quote_item["author"] = response.css('.author::text').get()
        yield quote_item

    def get_data(self, response:Response):
        for quote in response.css('.quote'):
            quote:  SelectorList
            author_url = quote.css('.quote a::attr(href)').get()
            print("author_url",author_url)
            next_page_url = response.urljoin(author_url)
            yield scrapy.Request(next_page_url, callback=self.set_author)   
            yield from self.set_quote(quote)

    def parse(self, response:Response):
        yield from self.get_data(response)
        next_page = response.css('li.next > a::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

        yield             



