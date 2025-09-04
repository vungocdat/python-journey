# STEP 5 - refactoring
# put scrape function into separate file and then save the scaping output into CSV file

import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from time import sleep


BASE_LINK = "https://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    link = "/page/1"
    while link:
        res = requests.get(f"{BASE_LINK}{link}")
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
        sleep(2)  # for studying purposes waiting is disabled
    return all_quotes


# write quotes to csv file
def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ("text", "author", "bio-link")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
