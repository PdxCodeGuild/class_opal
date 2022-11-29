""" 
mini capstone: Pokémon Face-Off 
"""

import requests
from pprint import pprint
import json


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
        print(f"New Pokemon created. {user_input} is an Electric type.")
        return ['electric']


# def retrieve_attack(pokemon_name):
#     '''
#     Returns the attack stat of the provided Pokémon.
#     '''
    
#     url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
#     response = requests.get(url)
    
#     response_text = response.json()
#     user_type = []
#     # pprint(response_text['stats'])
#     pprint(response_text['stats'])
#     pprint(user_type)
#     return user_type

# retrieve_attack('clefairy')


while True:

    pokename = str(input("Please enter your Pokémon: ").lower())
    pokerival = str(input("Please enter your rival's Pokémon: ").lower())
    user_types = [retrieve_type(pokename), retrieve_type(pokerival)]
    user1_type = user_types[0]
    user2_type = user_types[1]
    # user_types = [user_types, pokename, pokerival] <-- Do we even need that?
    break


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

        # pprint(relationsdict)
        return relationsdict


def modifier_calculator(user_name, relationsdict, type_lists, user_modifier=1.0):
    '''If user2's type is found in the list for user1, then that math
    is calculated to determine the strength of the Pokémon's attack.'''
    if type_lists in relationsdict["no_damage_to"]:
        # print(f"{user_name} deals no damage.")
        user_modifier *= 0
    if type_lists in relationsdict["quad_damage_to"]:
        # print(f"{user_name} deals 4x damage.")
        user_modifier *= 4
    if type_lists in relationsdict["double_damage_to"]:
        # print(f"{user_name} deals double damage.")
        user_modifier *= 2
    if type_lists in relationsdict["half_damage_to"]:
        # print(f"{user_name} deals half damage.")
        user_modifier *= 0.5
    else:
        # print(f"{user_name} dealt usual damage.")
        user_modifier *= 1.0

    return user_modifier


# def modifier_calculator(user_name, relationsdict, type_lists, user_modifier=1.0):
user1_modifier = modifier_calculator(pokename, find_type_relation(user1_type), user2_type[0])
user2_modifier = modifier_calculator(pokerival, find_type_relation(user2_type), user1_type[0])


def game(user1_modifier, user2_modifier, user1_health=100, user2_health=100, user1_def=100, user2_def=100, user1_attack=32.0, user2_attack=32.0):
    while user1_health > 0 and user2_health > 0:
        # print(f"User 1's health: {user1_health}")
        # print(f"User 2's health: {user2_health}")
        # The user attacks.
        user1_damage = round((user1_attack/user2_def * 2)/50 + 2 * user1_modifier, 0)
        # user2_health -= (user1_attack/user2_def/50 + 2 * user1_modifier)
        user2_health -= user1_damage
        # user2_health -= user1_attack * user1_modifier
        # Edgecases for how effective the attack was. This doesn't affect the damage, it's just for the user experience.
        if user1_modifier >= 2:
            print(f"{pokename}'s attack was supereffective! {pokename} dealt {user1_damage} damage.")
        if user1_modifier == 1:
            print(f"{pokename} dealt {user1_damage} damage.")
        if user1_modifier == 0.5:
            print(f"The attack wasn't very effective... {pokename} dealt {user1_damage} damage.")
        if user1_modifier == 0:
            print(f"The attack was not effective against {pokerival}.")
        # Print statements here in case first attack is the ending blow.    
        if user1_health <= 0 and user2_health <= 0:
            print("It's a tie!")
            break
        elif user2_health <= 0:
            print(f"{pokename} won!")
            break
        # User 2 attacks.
        user2_damage = round((user2_attack/user1_def * 2)/50 + 2 * user2_modifier, 0)
        user1_health -= user2_damage
        if user2_modifier >= 2:
            print(f"The attack was supereffective! {pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 1:
            print(f"{pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 0.5:
            print(f"The attack wasn't very effective... {pokerival} dealt {user2_damage} damage.")
        if user2_modifier == 0:
            print(f"The attack was not effective against {pokerival}.")
        if user1_health <= 0:
            print(f"{pokerival} won!")
            break
    # print(f"User 1's health: {user1_health}")
    # print(f"User 2's health: {user2_health}")


# user1_health = retrieve_hp(pokename)
# user2_health = retrieve_hp(pokerival)

# user1_attack = retrieve_attack(pokename)
# user2_attack = retrieve_attack(pokerival)


game(user1_modifier, user2_modifier, 38, 44, 40, 35, 41, 48)
# def game(user1_modifier, user2_modifier, user1_health=100, user2_health=100, user1_def=100, user2_def=100, user1_attack=32.0, user2_attack=32.0):
# game(user1_modifier, user2_modifier, user1_health, user2_health, user1_attack, user2_attack)
