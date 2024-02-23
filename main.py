import requests

api_key = "27bd06dfbd874fed8afa4a56fb49e3ec"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-01-23&sortBy=publishedAt&apiKey="\
    "27bd06dfbd874fed8afa4a56fb49e3ec"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])



