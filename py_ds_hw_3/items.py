import scrapy
    
class AuthorItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()
    def to_dict(self):
        return {
            'fullname': self['fullname'],
            'born_date': self['born_date'],
            'born_location': self['born_location'],
            'description': self['description']
        }
    

class QuoteItem(scrapy.Item):
    tags = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()
    def to_dict(self):
        return {
            'tags': self['tags'],
            'author': self['author'],
            'quote': self['quote'],
        }