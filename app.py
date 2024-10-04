import os
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Get the start_url from the POST request's JSON body
    start_url = request.json.get("start_url")
    if start_url:
        # Trigger the Scrapy spider with the provided URL
        subprocess.run(["scrapy", "crawl", "FortemSpider1", "-a", f"start_url={start_url}"])
        return {"message": "Spider started successfully!"}, 200
    return {"error": "No URL provided"}, 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if the PORT variable is not set
    app.run(host='0.0.0.0', port=port)  # Listen on all network interfaces
