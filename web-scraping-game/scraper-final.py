# STEP 5 - refactoring
# put scrape function into separate file and then save the scaping output into CSV file

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_LINK = "https://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename) as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes


def start_game(quotes):
    remaining_guesses = 4
    guess = ''

    quote = choice(quotes)
    print("Here's a quote:")
    print(quote["text"])
    print(quote["author"])  # for testing purposes show the answer

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(
            f"Who said this quote? Remaining guesses: {remaining_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print("That is correct! You win!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_LINK}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_location = soup.find(class_="author-born-location").get_text()
            print(
                f"Here's a hint: The author was born on {birth_date} {birth_location}")
        elif remaining_guesses == 2:
            first_name = quote["author"].split()[0]
            print(f"Here's a hint: Author's first name is {first_name}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split()[1][0]
            print(f"Here's a hint: Author's last name starts with {last_initial}")
        else:
            print("Sorry you run out of guesses.")
            print(f"The answer was {quote['author']}")

    # asking player to play again after the game is finished
    again = ''
    while again not in ("y", "yes", "n", "no"):
        again = input("Would you like to play again? (y/n) ").lower()

    if again in ("y", "yes"):
        return start_game(quotes)
    else:
        print("OK, bye!")


quotes = read_quotes("quotes.csv")
start_game(quotes)
