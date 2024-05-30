import http.client
import json
import random

# Function to get Pokémon data from the PokéAPI
def get_pokemon_data(pokemon_name):
    conn = http.client.HTTPSConnection("pokeapi.co")
    conn.request("GET", f"/api/v2/pokemon/{pokemon_name.lower()}")
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data)
    else:
        print(f"Error fetching data for {pokemon_name}: {response.reason}")
        return None

# Function to save Pokémon data to a file
def save_to_file(data, filename="pokemon_data.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

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
            random_pokemon = get_pokemon_data(str(random_id))
            if random_pokemon:
                pokemon_list.append(random_pokemon['name'])
                print(f"Random Pokémon added: {random_pokemon['name']}")
            else:
                print("Failed to retrieve a random Pokémon. Please try again.")
        else:
            data = get_pokemon_data(user_input)
            if data:
                pokemon_list.append(data['name'])
                print(f"Pokémon added: {data['name']}")
            else:
                print(f"No data found for Pokémon: {user_input}")

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
