# STEP 2 - scrap other pages

import requests
from bs4 import BeautifulSoup
from time import sleep  # needed so the program will wait between each scraping

# =============================================
# create a base URL so we can scrap other pages and update "res" variable
all_quotes = []
base_link = "https://quotes.toscrape.com"
link = "/page/1"

# put it all into while loop so the program will scrape all the pages
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
    # save the next page if next button exists
    link = next_button.find("a")["href"] if next_button else False
    sleep(2)

print(all_quotes)
