# STEP 3 - game logic

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_link = "https://quotes.toscrape.com"
link = "/page/1"

while link:
    res = requests.get(f"{base_link}{link}")
    print(f"Now scraping {base_link}{link} . . .")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
    next_button = soup.find(class_="next")
    link = next_button.find("a")["href"] if next_button else False
    # sleep(2)  # for studying purposes waiting is disabled

quote = choice(all_quotes)
print("Here's a quote:")
print(quote["text"])
