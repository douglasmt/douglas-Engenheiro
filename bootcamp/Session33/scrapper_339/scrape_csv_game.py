import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)
     

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here is a quote: ")
    print(quote["text"])
    print(quote["author"])

    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0 :
        guess = input(f"Who said this quote? Guesses remainin: {remaining_guesses}? \n")
        if guess.lower() == quote['author'].lower():
            print("you got it Right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser" )
            # print(soup.body)
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} in {birth_place}")

        elif remaining_guesses == 2:
            print(f"Here is a hint: The author's first name starts with { quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here is a hint: The author's last name starts with {last_initial }")
        else:        
            print(f"Sorry, you ran out of guesses. The answer was {quote['author'] }")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like do play again? (y/n)")
    if again.lower() in ('y', 'yes'):
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")

quotes = read_quotes("quotes.csv")
start_game(quotes)
