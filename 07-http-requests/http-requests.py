import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})

#print(response.text) # type is str
#print(response.json()) # returns a python dictionary

data = response.json()

print(data["joke"])
