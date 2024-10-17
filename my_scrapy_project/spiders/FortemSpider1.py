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
            if url:
                yield SplashRequest(url, self.deep_parse, args={'wait': 2}, errback=self.handle_error)

        # Shallow scraping for website 2
        for url in self.start_urls_2:
            if url:
                yield SplashRequest(url, self.shallow_parse, args={'wait': 2}, errback=self.handle_error)

    def deep_parse(self, response):
        """ Deep scraping logic for website 1 """
        self.logger.info(f'Deep scraping: {response.url}')

        # Extract data
        page_title = response.css('title::text').get(default='No Title')
        paragraphs = response.css('p::text').getall()
        images = response.css('img::attr(src)').getall()

        # Follow links for deeper scraping, limit depth to avoid infinite crawling
        for next_page in response.css('a::attr(href)').getall():
            next_page = response.urljoin(next_page)
            if self.allowed_domains and self.allowed_domains[0] in next_page:
                yield SplashRequest(next_page, self.deep_parse, args={'wait': 2}, errback=self.handle_error)

        # Return the scraped data
        yield {
            'url': response.url,
            'title': page_title,
            'paragraphs': paragraphs,
            'images': images
        }

    def shallow_parse(self, response):
        """ Shallow scraping logic for website 2 """
        self.logger.info(f'Shallow scraping: {response.url}')

        # Extract data
        page_title = response.css('title::text').get(default='No Title')
        paragraphs = response.css('p::text').getall()

        # Return the scraped data
        yield {
            'url': response.url,
            'title': page_title,
            'paragraphs': paragraphs
        }

    def handle_error(self, failure):
        """ Handle errors during scraping """
        self.logger.error(f"Error on {failure.request.url}: {failure.value}")
