# Define here the models for your scraped items
from scrapy.item import Item, Field

class BookcrawltwoItem(Item):
    title = Field()
    category = Field()
    description = Field()
    price = Field()
