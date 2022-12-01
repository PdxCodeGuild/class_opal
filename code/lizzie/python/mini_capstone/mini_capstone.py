""" 
mini capstone: Pokémon Face-Off 
"""

from pprint import pprint
import json
from PIL import Image
import requests


def retrieve_type(user_input):
    '''
    Returns a list of strings including each pokemon's type
    using the name of the pokemon given by the user.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{user_input}/'    # Using user's input as an endpoint to return that Pokémon's type

    response = requests.get(url)
    try:
        response_text = response.json()
        user_type = []
        for slot in response_text['types']:         # Going into list of dictionaries and retrieving relevant data.
            user_type.append(slot['type']['name'])  # Appends each type to list (e.g. ['water', 'ice'])
        return user_type
    except json.decoder.JSONDecodeError:
        # If the user provides an invalid name, default stats and a type are assigned.
        print(f"New Pokemon created. {user_input} is an Electric type.")
        return ['electric']


def retrieve_hp(pokemon_name):
    '''
    Returns the health stat of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    
    try:
        response_text_hp = response.json()
        user_hp = response_text_hp['stats'][0]['base_stat']
        return user_hp
    except json.decoder.JSONDecodeError:
        return 35


def retrieve_attack(pokemon_name):
    '''
    Returns the attack stat of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    
    try:
        response_text_attack = response.json()
        user_attack = response_text_attack['stats'][1]['base_stat']
        return user_attack
    except json.decoder.JSONDecodeError:
        return 55


def retrieve_defense(pokemon_name):
    '''
    Returns the attack stat of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    
    try:
        response_text_defense = response.json()
        user_defense = response_text_defense['stats'][2]['base_stat']
        return user_defense
    except json.decoder.JSONDecodeError:
        return 40


def find_type_relation(user_types: list):
        '''
        Uses pokeapi to determine the relationship of the given type to all other types.
        Returns a dictionary of four lists with the following keys: 'half_damage_to', 
        'no_damage_to', 'double_damage_to', and 'quad_damage_to'.
        '''
        relationsdict = {
            "half_damage_to": [],
            "no_damage_to": [],
            "double_damage_to": [],
            "quad_damage_to": []
        }

        for user_type in user_types:
            
            url = f'https://pokeapi.co/api/v2/type/{user_type}/'

            response = requests.get(url)
            response_text = response.json()

            for name in response_text['damage_relations']['half_damage_to']:
                if name['name'] not in relationsdict['half_damage_to']:
                    relationsdict['half_damage_to'].append(name['name'])
            for name in response_text['damage_relations']['no_damage_to']:
                if name['name'] not in relationsdict['no_damage_to']:
                    relationsdict['no_damage_to'].append(name['name'])
            for name in response_text['damage_relations']['double_damage_to']:
                # If it is already in the dictionary, both types stack and deal more damage.
                if name['name'] in relationsdict["double_damage_to"]:
                    relationsdict['quad_damage_to'].append(name['name'])
                if name['name'] not in relationsdict['double_damage_to']:
                    relationsdict['double_damage_to'].append(name['name'])
        return relationsdict


def modifier_calculator(relationsdict, type_lists, user_modifier=1.0):
    '''If user2's type is found in the list for user1, then that math
    is calculated to determine the strength of the Pokémon's attack.'''
    if type_lists in relationsdict["no_damage_to"]:
        user_modifier *= 0
    if type_lists in relationsdict["quad_damage_to"]:
        user_modifier *= 4
    if type_lists in relationsdict["double_damage_to"]:
        user_modifier *= 2
    if type_lists in relationsdict["half_damage_to"]:
        user_modifier *= 0.5
    else:
        user_modifier *= 1.0
    return user_modifier


def retrieve_image(pokemon_name):
    '''
    Returns an image of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)

    try:
        response_text = response.json()
        pokemonlink = response_text['sprites']['front_default']         # Accessing the url of the front-facing sprite.
        img = Image.open(requests.get(pokemonlink, stream = True).raw)  # Retrieving the url.
        img.save(f'{pokemon_name}.png')                 # Saving the image as a .png file where the terminal is pointed.
        show_image = Image.open(f'{pokemon_name}.png')  # Retrieving the image from its saved place on your computer. 
        show_image = show_image.convert('RGB')          # Convert image to correct filetype in order to show it.
        show_image.show()       # Opens the file in your default image viewer.
    except requests.exceptions.JSONDecodeError: # If a custom-made Pokémon is involved, skip image retrieval.
        return None


def game(user1_modifier=1, user2_modifier=1, user1_health=35.0, user2_health=35.0, user1_def=40.0, user2_def=40.0, user1_attack=55.0, user2_attack=55.0):
    # Call the retrieve_image function to retrieve pictures of the two Pokémon.
    retrieve_image(pokename)
    retrieve_image(pokerival)
    # To create a health bar, storing the user healths as new variables.
    user1_max_health = user1_health
    user2_max_health = user2_health
    healthDashes = 12


    def health_bar(user_max_health, user_health, name):
        dashConvert = int(user_max_health/healthDashes)     # Get the number to divide by to convert health to dashes
        currentDashes = int(user_health/dashConvert)        # Current dashes decided 
        remainingHealth = healthDashes - currentDashes      # Remaining health will fill space.
        healthDisplay = '-' * currentDashes                 # Convert dashes into a string:   "--------"
        remainingDisplay = ' ' * remainingHealth            # Convert spaces into a string: "            "
        if user_health <= 0:
            remainingDisplay = ' '
        percent = str(int((user_health/user_max_health)*100)) + "%"     # Get the percent as a whole number

        print("|" + healthDisplay + remainingDisplay + "|") # Print out textbased healthbar
        print(f'       {name}')
        print(f"        {percent}")


    while user1_health > 0 and user2_health > 0:                # While both Pokémon have health, they fight.
        user1_damage = round(25 * user1_attack/user2_def * user1_modifier + 1, 0)   # The user attacks using a fomula to determine damage.
        user2_health -= user1_damage
        health_bar(user1_max_health, user1_health, pokename)    # Displays the health bar after every user attacks.
        health_bar(user2_max_health, user2_health, pokerival)
        # Edgecases for how effective the attack was. This doesn't affect the damage, it's just for the user experience.
        if user1_modifier == 0 and user2_modifier == 0:
            # If both Pokémon are incapable of attacking each other, run this print statement and end the fight.
            print(f"Neither move is effective. It seems {pokename} and {pokerival} are in an eternal standoff...")
            break  
        if user1_modifier >= 2:
            print(f"{pokename}'s attack was supereffective! {pokename} dealt {user1_damage} damage.\n")
        if user1_modifier == 1:
            print(f"{pokename} dealt {user1_damage} damage.\n")
        if user1_modifier == 0.5:
            print(f"{pokename}'s attack wasn't very effective... {pokename} dealt {user1_damage} damage.\n")
        if user1_modifier == 0:
            print(f"{pokename}'s attack was not effective against {pokerival}.\n")
        # Print statements here in case first attack is the ending blow. 
        if user1_health <= 0 and user2_health <= 0:
            print("It's a tie!")
            break
        elif user2_health <= 0:     # If user2 faints, run pokename as the winner.
            print(f"{pokename} won!")
            break
        # User 2 attacks.
        user2_damage = round(25 * user2_attack/user1_def * user2_modifier + 1, 0)
        user1_health -= user2_damage
        health_bar(user1_max_health, user1_health, pokename)
        health_bar(user2_max_health, user2_health, pokerival)
        if user2_modifier >= 2:
            print(f"{pokerival}'s attack was supereffective! {pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 1:
            print(f"{pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 0.5:
            print(f"{pokerival}'s attack wasn't very effective... {pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 0:
            print(f"{pokerival}'s attack was not effective against {pokename}.")
        # Other print statement following user2's attack in case it ends the fight.
        if user1_health <= 0:
            print(f"{pokerival} won!")
            break


pokename = str(input("Please enter your Pokémon: ").lower())
pokerival = str(input("Please enter your rival's Pokémon: ").lower())
user_types = [retrieve_type(pokename), retrieve_type(pokerival)]    # Assigns a list of lists containing the users' types. Ex.: [['fire'], ['ice', 'water']]
user1_type = user_types[0]      # Assigns the first list of types to user1_type. Ex.: ['fire']
user2_type = user_types[1]      # Assigns the second list of types to user1_type. Ex.: ['ice', 'water']


# Storing all the variables we need in a dictionary and passing them through the game() function as keyword arguments.
pokemon_kwargs = {
    'user1_modifier': modifier_calculator(find_type_relation(user1_type), user2_type[0]),
    'user2_modifier': modifier_calculator(find_type_relation(user2_type), user1_type[0]),
    'user1_health': retrieve_hp(pokename),
    'user2_health': retrieve_hp(pokerival),
    'user1_attack': retrieve_attack(pokename),
    'user2_attack': retrieve_attack(pokerival),
    'user1_def': retrieve_defense(pokename),
    'user2_def': retrieve_defense(pokerival)
}

game(**pokemon_kwargs)
