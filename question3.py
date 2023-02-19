""" Question 3
In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
retrieve multiple Pokemon and save their names and moves to a file.
Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
Pokemon. Save their names and moves into a file called 'pokemon.txt'

Steps: set up a list with 6 pokemon IDs
create a for loop, call the API to retrieve the data in each pokemon
open and write a file called "pokemon.txt"
Save the Pokemon names and moves in that file
 """
import requests  # To work with the Requests library in Python, we must import the appropriate module.
# utility module that can be used to print data structures in a readable way
from pprint import pprint

""" The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
To use pprint, begin by importing the library at the top of your Python file. From here you can either use the . pprint() method or instantiate your own pprint object with PrettyPrinter() """
# Install requests library using pip.
# List of Pokemon IDs.
pokemon_ID = [2, 4, 17, 29, 145, 905]

with open('pokemon.txt', 'w+') as pokemon_file:
    # Loop through list of Pokemon IDs, using API to get the name and move data for each ID,
    # and write data to pokemon.txt file.

    for number in pokemon_ID:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}/'
        # response.url returns the URL of the response. The get() method sends a GET request to the specified url
        response = requests.get(url)
        print(response)
        pokemon = response.json()
        pokemon_name = pokemon['name']
        pokemon_file.write(f'\n{pokemon_name}:\n')
        print(pokemon_name)

        moves = pokemon['moves']
        for move in moves:
            pokemon_move = move['move']['name']
            pokemon_file.write(f'{pokemon_move}\n')
            print(pokemon_move)
