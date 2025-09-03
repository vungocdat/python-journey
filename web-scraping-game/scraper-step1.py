# STEP 1 - scrape the website with quotes

import requests
from bs4 import BeautifulSoup

# scrape the website (only one page)
link = "https://quotes.toscrape.com"
res = requests.get(link)
soup = BeautifulSoup(res.text, "html.parser")

# print(soup.body) # now we can see the whole body of the page

# now filter to get just all quotes
quotes = soup.find_all(class_="quote")
# print(quotes)

# get only the quote - text
# for quote in quotes:
#    print(quote.find(class_="text").get_text())

# since now we know how to extract the text, it is time to save quotes
# into the list in form of dictionaries - quotes and author
all_quotes = []
for quote in quotes:
    all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"] # access to the link of authors bio
        })
# print(all_quotes)

# Scrapping one page is done. Now we need to find a way to scrap the rest of
# the pages by inspecting the "next" button
next_button = soup.find(class_="next")
# print(next_button)
print(next_button.find("a")["href"])

# to be continued in STEP 2
