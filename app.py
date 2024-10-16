from flask import Flask, request, jsonify
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from my_scrapy_project.spiders.FortemSpider1 import FortemSpider1  # Adjust the import for your spider

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Get the URLs from the JSON body of the request
    start_url_1 = request.json.get('start_url_1')
    start_url_2 = request.json.get('start_url_2')

    # Check if URLs are provided
    if not start_url_1 or not start_url_2:
        return jsonify({"error": "No URL provided"}), 400

    # Create a method to run the Scrapy spider
    def run_spider(start_url_1, start_url_2):
        process = CrawlerProcess(get_project_settings())
        process.crawl(FortemSpider1, start_url_1=start_url_1, start_url_2=start_url_2)
        process.start(stop_after_crawl=False)

    # Run the Scrapy spider with the provided URLs
    reactor._handleSignals = False  # Disable signal handling for Scrapy in a headless environment
    run_spider(start_url_1, start_url_2)

    return jsonify({"message": "Spider started successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
