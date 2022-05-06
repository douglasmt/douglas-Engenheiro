import requests
import pyfiglet
import termcolor
from random import choice # chooses one of the responses 

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="magenta")
print(header)

term = input("Let me tell you a joke! Give me a topic: ")
# term will be used in get request

response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"}, # https://icanhazdadjoke.com/api
    params={"term": term}                   # EXAMPLE: "term":"cat", limit=1
).json()

# response_json.json()

# Example in the browser
# https://icanhazdadjoke.com/search?term=cat&limit=2
# page, search for the term and maximum of 2 results

results = response_json["results"]
total_jokes = response_json["total_jokes"] # restults count
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke'] # uses a random choice
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke'] # takes the first item with a joke
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
