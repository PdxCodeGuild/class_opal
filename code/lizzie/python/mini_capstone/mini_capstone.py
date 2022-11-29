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
    url = f'https://pokeapi.co/api/v2/pokemon/{user_input}/'

    response = requests.get(url)
    try:
        response_text = response.json()
        user_type = []
        for slot in response_text['types']:
            user_type.append(slot['type']['name'])
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
    
    response_text_hp = response.json()
    user_hp = response_text_hp['stats'][0]['base_stat']
    return user_hp


def retrieve_attack(pokemon_name):
    '''
    Returns the attack stat of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    
    response_text_attack = response.json()
    user_attack = response_text_attack['stats'][1]['base_stat']
    return user_attack


def retrieve_defense(pokemon_name):
    '''
    Returns the attack stat of the provided Pokémon.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    
    response_text_defense = response.json()
    user_defense = response_text_defense['stats'][2]['base_stat']
    return user_defense


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


def game(user1_modifier=1, user2_modifier=1, user1_health=32.0, user2_health=32.0, user1_def=30.0, user2_def=30.0, user1_attack=32.0, user2_attack=32.0):
    # While both Pokémon have health, they fight.
    while user1_health > 0 and user2_health > 0:
        # The user attacks using a fomula to determine damage.
        user1_damage = round(user1_attack/user2_def * 2/50 + 2 * user1_modifier, 0)
        user2_health -= user1_damage
        # Edgecases for how effective the attack was. This doesn't affect the damage, it's just for the user experience.
        if user1_modifier == 0 and user2_modifier == 0:
            # If both Pokémon are incapable of attacking each other, run this print statement and end the fight.
            print(f"Neither move is effective. It seems {pokename} and {pokerival} are in an eternal standoff...")
            break  
        if user1_modifier >= 2:
            print(f"{pokename}'s attack was supereffective! {pokename} dealt {user1_damage} damage.")
        if user1_modifier == 1:
            print(f"{pokename} dealt {user1_damage} damage.")
        if user1_modifier == 0.5:
            print(f"{pokename}'s attack wasn't very effective... {pokename} dealt {user1_damage} damage.")
        if user1_modifier == 0:
            print(f"{pokename}'s attack was not effective against {pokerival}.")
        # Print statements here in case first attack is the ending blow. 
        if user1_health <= 0 and user2_health <= 0:
            print("It's a tie!")
            break
        elif user2_health <= 0:
            print(f"{pokename} won!")
            break
        # User 2 attacks.
        user2_damage = round(user2_attack/user1_def * 2/50 + 2 * user2_modifier, 0)
        user1_health -= user2_damage
        if user2_modifier >= 2:
            print(f"{pokerival}'s attack was supereffective! {pokerival} dealt {user2_damage} damage.\n")
        if user2_modifier == 1:
            print(f"{pokerival} dealt {user2_damage} damage.\n")
        if user2_modifier == 0.5:
            print(f"{pokerival}'s attack wasn't very effective... {pokerival} dealt {user2_damage} damage.\n")
        if user2_modifier == 0:
            print(f"{pokerival}'s attack was not effective against {pokerival}.\n")
        # Other print statement following user2's attack in case it ends the fight.
        if user1_health <= 0:
            print(f"{pokerival} won!")
            break


# pokename = str(input("Please enter your Pokémon: ").lower())
# pokerival = str(input("Please enter your rival's Pokémon: ").lower())
# user_types = [retrieve_type(pokename), retrieve_type(pokerival)]
# user1_type = user_types[0]
# user2_type = user_types[1]


# pokemon_kwargs = {
#     'user1_modifier': modifier_calculator(find_type_relation(user1_type), user2_type[0]),
#     'user2_modifier': modifier_calculator(find_type_relation(user2_type), user1_type[0]),
#     'user1_health': retrieve_hp(pokename),
#     'user2_health': retrieve_hp(pokerival),
#     'user1_attack': retrieve_attack(pokename),
#     'user2_attack': retrieve_attack(pokerival),
#     'user1_def': retrieve_defense(pokename),
#     'user2_def': retrieve_defense(pokerival)
# }

# game(**pokemon_kwargs)

pokemon_name = 'pikachu'
# def retrieve_image(pokemon_name):
'''
Returns an image of the provided Pokémon.
'''
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'


response = requests.get(url)

response_text = response.json()
pokeimage = response_text['sprites']['front_default']
# with Image.open(pokeimage) as img:
#     img.show()
pprint(pokeimage)

# response_text_attack = response.json()
# user_attack = response_text_attack['stats'][1]['base_stat']
# user_hp = response_text_hp['stats'][0]['base_stat']

