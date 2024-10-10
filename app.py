from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/start_spider', methods=['POST'])
def start_spider():
    # Get the URLs from the JSON body of the request
    start_url_1 = request.json.get('start_url_1')
    start_url_2 = request.json.get('start_url_2')

    # Check if URLs are provided
    if not start_url_1 or not start_url_2:
        return jsonify({"error": "No URL provided"}), 400

    # Run the Scrapy spider with the provided URLs
    os.system(f"scrapy crawl dual_scraper -a start_url_1={start_url_1} -a start_url_2={start_url_2}")

    return jsonify({"message": "Spider started successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
