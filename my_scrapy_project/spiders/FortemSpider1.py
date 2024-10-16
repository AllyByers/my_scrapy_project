import scrapy
from scrapy_splash import SplashRequest

class FortemSpider1(scrapy.Spider):
    name = "fortem_scraper_1"

    def __init__(self, start_url_1=None, start_url_2=None, *args, **kwargs):
        super(FortemSpider1, self).__init__(*args, **kwargs)
        self.start_urls_1 = [start_url_1] if start_url_1 else []
        self.start_urls_2 = [start_url_2] if start_url_2 else []

    def start_requests(self):
        # Deep scraping for website 1
        for url in self.start_urls_1:
            yield SplashRequest(url, self.deep_parse, args={'wait': 2})

        # Shallow scraping for website 2
        for url in self.start_urls_2:
            yield SplashRequest(url, self.shallow_parse, args={'wait': 2})

    def deep_parse(self, response):
        # Deep scraping logic for website 1
        self.logger.info(f'Deep scraping: {response.url}')
        page_title = response.css('title::text').get()
        paragraphs = response.css('p::text').getall()
        images = response.css('img::attr(src)').getall()

        # Follow links for deeper scraping
        for next_page in response.css('a::attr(href)').getall():
            next_page = response.urljoin(next_page)
            if self.allowed_domains and self.allowed_domains[0] in next_page:
                yield SplashRequest(next_page, self.deep_parse, args={'wait': 2})

        yield {
            'url': response.url,
            'title': page_title,
            'paragraphs': paragraphs,
            'images': images
        }

    def shallow_parse(self, response):
        # Shallow scraping logic for website 2
        self.logger.info(f'Shallow scraping: {response.url}')
        page_title = response.css('title::text').get()
        paragraphs = response.css('p::text').getall()

        yield {
            'url': response.url,
            'title': page_title,
            'paragraphs': paragraphs
        }
