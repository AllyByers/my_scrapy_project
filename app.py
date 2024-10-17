from flask import Flask, request, jsonify
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from crochet import setup, run_in_reactor
from my_scrapy_project.spiders.FortemSpider1 import FortemSpider1

# Initialize Crochet
setup()

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

    # Run the Scrapy spider asynchronously using Crochet
    run_spider(start_url_1, start_url_2)

    return jsonify({"message": "Spider started successfully"}), 200

@run_in_reactor
def run_spider(start_url_1, start_url_2):
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(FortemSpider1, start_url_1=start_url_1, start_url_2=start_url_2)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Default to port 5000 if not set
    app.run(debug=True, host='0.0.0.0', port=port)