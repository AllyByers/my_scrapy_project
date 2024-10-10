from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    start_url_1 = request.json.get('start_url_1')
    start_url_2 = request.json.get('start_url_2')

    # Trigger the Scrapy spider with dynamic URLs
    os.system(f"scrapy crawl dual_scraper -a start_url_1={start_url_1} -a start_url_2={start_url_2}")

    return {"message": "Spider started successfully"}, 200
