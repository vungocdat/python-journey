import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD JOKE 3000")
colored_header = colored(header, "cyan", attrs=["blink"])
print(colored_header)

search_joke = input("What would you like to search for? ")

url = "https://icanhazdadjoke.com/search"

res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={
            "term": search_joke
        }
).json()

num_jokes = res['total_jokes']
results = res['results']

if num_jokes > 1:
    print(f"There are {num_jokes} jokes about {search_joke}. Here is one:")
    # choosing random joke from the list of jokes
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"There is 1 joke about {search_joke}. Here it is:")
    print(results[0]['joke'])
else:
    print(f"Sorry, there are no jokes about {search_joke}.")
