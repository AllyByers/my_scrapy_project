from flask import Flask, request, jsonify
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from my_scrapy_project.spiders.FortemSpider1 import FortemSpider1  # Adjust the import for your spider

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Ensure that the request body contains JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Get the URLs from the JSON body of the request
    data = request.get_json()
    start_url_1 = data.get('start_url_1')
    start_url_2 = data.get('start_url_2')

    # Check if URLs are provided
    if not start_url_1 or not start_url_2:
        return jsonify({"error": "Both start_url_1 and start_url_2 must be provided"}), 400

    # Create a method to run the Scrapy spider
    def run_spider(start_url_1, start_url_2):
        process = CrawlerProcess(get_project_settings())
        process.crawl(FortemSpider1, start_url_1=start_url_1, start_url_2=start_url_2)
        process.start()

    # Run the Scrapy spider with the provided URLs
    run_spider(start_url_1, start_url_2)

    return jsonify({"message": "Spider started successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
