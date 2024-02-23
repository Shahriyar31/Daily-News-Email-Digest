import requests
from send_email import send_email

api_key = "27bd06dfbd874fed8afa4a56fb49e3ec"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-01-23&sortBy=publishedAt&apiKey="\
    "27bd06dfbd874fed8afa4a56fb49e3ec"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)




