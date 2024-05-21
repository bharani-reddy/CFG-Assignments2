import requests
import random
import json

# Function to get Pokémon data from the PokéAPI
def get_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to save Pokémon data to a file
def save_to_file(data, filename="pokemon_data.txt"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Main function to interact with the user and process Pokémon data
def main():
    print("Welcome to the Pokémon Info App!")
    pokemon_list = []

    while True:
        user_input = input("Enter a Pokémon name (or 'random' for a random Pokémon, 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        elif user_input.lower() == 'random':
            random_id = random.randint(1, 151)
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_id}")
            if response.status_code == 200:
                data = response.json()
                pokemon_list.append(data['name'])
            else:
                print("Failed to retrieve a random Pokémon. Please try again.")
        else:
            pokemon_list.append(user_input)

    # Ensure Pikachu is included
    if "pikachu" not in pokemon_list:
        pokemon_list.append("pikachu")
        print("Pikachu has been added to your list!")

    pokemon_data = {}
    for pokemon in pokemon_list:
        data = get_pokemon_data(pokemon)
        if data:
            pokemon_data[pokemon] = {
                "name": data['name'],
                "moves": [move['move']['name'] for move in data['moves']]
            }
        else:
            print(f"Could not find data for Pokémon: {pokemon}")

    save_to_file(pokemon_data)
    print(f"Pokémon data saved to file. You retrieved {len(pokemon_data)} Pokémon.")

if __name__ == "__main__":
    main()
