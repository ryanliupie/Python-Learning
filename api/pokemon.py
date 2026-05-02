# Learning how to connect to an API in Python (Bro Code example) 
# go to this website "https://pokeapi.co/"

import requests # separate library that handles complexities of making HTTP requests 

base_url = "https://pokeapi.co/api/v2/" # this stores the starting address of the PokeAPI. Every API request beings with this URL

def get_pokemon_info(name): 
    url = f"{base_url}/pokemon/{name}" # this builds the full web address for the specific pokemon. if we pass in pikachu, the URL becomes https://pokeapi.co/api/v2/pokemon/pikachu
    response = requests.get(url) # Actual moment of contact; program reaches to internet, knocks on URL, and waits for API to respond. Result gets stored in "response"

    if response.status_code == 200: # status code 200 = everything worked 
        pokemon_data = response.json() # turns API response into JSON; allows python to work with data better 
        return pokemon_data 
    else: 
        print(f"Failed to retrieve data{response.status_code}")

pokemon_info = get_pokemon_info("pikachu") # this passes the pokemon name into the function and calls it

if pokemon_info: 
    print(f"{pokemon_info["name"]}")