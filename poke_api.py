"""Poke API connection"""

# Utilities
import requests

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    """GET the pokemons from pokeapi"""    

    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        for pokemon in results:
            name = pokemon['name']
            print(name)

        next = input("Do you want to continue? [Y/N]: ").lower()

        if next == 'y':
            get_pokemons(offset=offset + 20)


if __name__ == '__main__':
    """Main function"""

    url='https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()
