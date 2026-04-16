import requests
from bs4 import BeautifulSoup

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight"

# make request
result = requests.get(url)
data = BeautifulSoup(result.text, "html.parser")

# getting required data
heading = data.find("h1").text
author = data.find("a", {"data-qa": "author-name"}).text
byline = data.find("div", {"data-qa": "author-byline"})
updated_at = data.find("div", {"data-qa": "timestamp"}).text


content = data.find_all("div", {"data-qa": "article-body"})


for line in content:
    print(line.text)

print(heading)
print(author)
print(byline)
print(updated_at)
