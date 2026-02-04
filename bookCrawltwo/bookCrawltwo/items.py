# Define here the models for your scraped items
from scrapy.item import Item, Field

class BookcrawltwoItem(Item):
    pass

def seralize_price(value):
    return f"${str(value)}"

class BookItem(Item):
    url = Field()
    title = Field()
    upc = Field()
    product_type = Field()
    # price_excl_tax = Field(serializer = seralize_price)
    price_excl_tax = Field()
    price_incl_tax = Field()
    tax = Field()
    availability = Field()
    num_reviews = Field()
    stars = Field()
    category = Field()
    description = Field()
    price = Field()