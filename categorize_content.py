import spacy
import json

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

# Define keywords for categorization
keywords = {
    "sustainability": [
        "sustainability", "green", "renewable", "eco-friendly", "carbon footprint",
        "retrofit", "decarbonisation"  # Added new keywords
    ],
    "housing repairs": [
        "repairs", "maintenance", "plumbing", "electrical", "renovation"
    ],
    "capital works": [
        "infrastructure", "construction", "development", "expansion", "capital improvement",
        "investment", "asset management", "public works", "facilities", "building projects"
    ]
}

# Function to categorize content
def categorize_content(text, keywords):
    doc = nlp(text.lower())
    category_scores = {category: 0 for category in keywords}

    for token in doc:
        for category, words in keywords.items():
            if token.text in words:
                category_scores[category] += 1

    best_category = max(category_scores, key=category_scores.get)
    return best_category if category_scores[best_category] > 0 else "Uncategorized"

# Load scraped data from JSON file
with open('scraped_data.json', 'r', encoding='utf-8') as f:
    scraped_data = json.load(f)

# Categorize each piece of content
for item in scraped_data:
    content = item["content"]
    category = categorize_content(content, keywords)
    item["category"] = category

# Output categorized data
for item in scraped_data:
    print(f"Title: {item['title']}, Category: {item['category']}")

# Optionally, save the categorized data back to a JSON file
with open("categorized_data.json", "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, indent=4)
