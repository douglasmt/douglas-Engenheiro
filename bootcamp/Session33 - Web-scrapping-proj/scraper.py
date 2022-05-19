import requests
from bs4 import BeautifulSoup

all_quotes = []
base_url = "http://quotes.toscrape.com/"
url = "/page/1"

res = requests.get(f"{base_url}{url}")
soup = BeautifulSoup(res.text, "html.parser") 
#  GuessedAtParserWarning: No parser was explicitly specified, 
# so I'm using the best available HTML parser for this system ("lxml"). 

quotes = soup.find_all(class_="quote")

for quote in quotes:
    all_quotes.append({
        "text": quote.find(class_="text").get_text(),
        "author": quote.find(class_="author").get_text(),
        "bio-link": quote.find("a")["href"]
    })

next_button = soup.find(class_="next")
print(next_button.find("a")["href"])