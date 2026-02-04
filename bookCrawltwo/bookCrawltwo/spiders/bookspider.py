from itertools import product
import scrapy
from bookCrawltwo.items import BookcrawltwoItem

class BookSpider(scrapy.Spider):
    name = "bookstwo"
    allowed_domains = ['books.toscrape.com']
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            yield {
                'name': book.css("h3 a::text").get(),
                'price': book.css(".product_price .price_color::text").re_first(r"\d+\.\d+"),
                'url': book.css("h3 a").attrib['href']
            }
        next_page = response.css("li.next a ::attr(href)").get()

        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = "http://books.toscrape.com/" + next_page
            else:
                next_page_url = "http://books.toscrape.com/catalogue/" + next_page

            yield response.follow(next_page_url, callback = self.parse)


    # custom_settings = {
    #     "FEEDS": {"data.csv" : {"format": "csv",}}
    # }

    # def start_requests(self):
    #     url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    #     yield scrapy.Request(url, callback=self.parse)

    # def parse(self, response):
    #     product = response.css("div.product_main")

    #     book_item = BookcrawltwoItem()

    #     book_item["title"] = product.css("h1::text").extract_first()
    #     book_item["category"] = product.css("h1::text").extract_first()
    #     book_item["title"] = product.css("h1::text").extract_first()
    #     book_item["title"] = product.css("h1::text").extract_first()
