from flask import Flask, request, jsonify
import os
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet.defer import inlineCallbacks
from crochet import setup, wait_for

# Initialize Crochet for asynchronous event handling
setup()

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Get the URLs from the JSON body of the request
    start_url_1 = request.json.get('start_url_1')
    start_url_2 = request.json.get('start_url_2')

    # Check if URLs are provided
    if not start_url_1 or not start_url_2:
        return jsonify({"error": "No URL provided"}), 400

    # Run the Scrapy spider asynchronously using Crochet with increased timeout
    run_spider_async(start_url_1, start_url_2)

    return jsonify({"message": "Spider started successfully"}), 200

@wait_for(timeout=3600)  # Wait for up to 1 hour for the spider to complete
@inlineCallbacks  # Required to use Scrapy's crawl process with Twisted
def run_spider_async(start_url_1, start_url_2):
    try:
        settings = get_project_settings()
        runner = CrawlerRunner(settings)
        yield runner.crawl('fortem_scraper', start_url_1=start_url_1, start_url_2=start_url_2)
    except Exception as e:
        print(f"Error running spider: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
