import requests
from bs4 import BeautifulSoup

news_url = (
    "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
)

# Req
res = requests.get(news_url)
data = BeautifulSoup(res.text, "html.parser")

# Data
heading = data.find("h1").text
byline = data.find(class_="Article__subtitle").text
author = byline.split(" • ")[0]
updated_at = byline.split(" • ")[1]

print("Heading =", heading)
print("Author =", author)
print("Last updated at =", updated_at.split("Updated ")[1])
print("Byline = ", byline)
print()

paragraphs = data.find_all(class_="Paragraph__component")

for i in range(len(paragraphs)):
    cont = paragraphs[i].get_text()
    print(cont, end="\n\n")
