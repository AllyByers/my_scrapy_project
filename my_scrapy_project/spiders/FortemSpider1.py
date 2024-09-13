import scrapy

class FortemSpider1(scrapy.Spider):
    name = "FortemSpider1"
    allowed_domains = ["fortem.co.uk"]
    start_urls = ["https://www.fortem.co.uk/"]

    def parse(self, response):
        # Extract title of the page
        page_title = response.css('title::text').get()
        
        # Extract all paragraphs
        paragraphs = response.css('p::text').getall()
        
        # Extract all image URLs
        image_urls = response.css('img::attr(src)').getall()

        # Store extracted data
        yield {
            'title': page_title,
            'paragraphs': paragraphs,
            'images': image_urls
        }

        # Follow links to next pages
        for next_page in response.css('a::attr(href)').getall():
            # Clean up the next_page URL and make sure it stays within the domain
            next_page = response.urljoin(next_page)
            
            # Only follow links that are within the allowed domain
            if self.allowed_domains[0] in next_page:
                yield scrapy.Request(next_page, callback=self.parse)
