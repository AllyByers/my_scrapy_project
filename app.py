from flask import Flask, request, jsonify
import os
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from my_scrapy_project.spiders.FortemSpider1 import FortemSpider1  # Adjust the import for your spider
from twisted.internet.defer import inlineCallbacks
from crochet import setup, wait_for

setup()  # Initialize crochet for asynchronous event handling with Twisted

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Get the URLs from the JSON body of the request
    start_url_1 = request.json.get('start_url_1')
    start_url_2 = request.json.get('start_url_2')

    # Check if URLs are provided
    if not start_url_1 or not start_url_2:
        return jsonify({"error": "No URL provided"}), 400

    # Run the Scrapy spider asynchronously using Crochet
    run_spider_async(start_url_1, start_url_2)

    return jsonify({"message": "Spider started successfully"}), 200

@wait_for(20)  # Wait for the spider to finish before returning the response
@inlineCallbacks  # Required to use Scrapy's crawl process with Twisted
def run_spider_async(start_url_1, start_url_2):
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    yield runner.crawl(FortemSpider1, start_url_1=start_url_1, start_url_2=start_url_2)

if __name__ == '__main__':
    app.run(debug=True)
