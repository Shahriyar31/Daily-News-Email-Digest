import requests
from send_email import send_email

topic = "tesla"

api_key = "27bd06dfbd874fed8afa4a56fb49e3ec"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&" \
      "from=2024-01-23&" \
      "sortBy=publishedAt&" \
      "apiKey=27bd06dfbd874fed8afa4a56fb49e3ec&" \
      "language=en"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)




