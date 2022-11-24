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
        # Trying to handle making a new pokemon with a type that's
        # Found in the list.
        # chosen_type = str(input('Please provide a type: '))
        # if chosen_type in response_text:
        #     return [chosen_type]
        # else:
        print(f"New Pokemon created. {user_input} is an Electric type.")
        return ['electric']


while True:
    # user is being assigned the list of types returned from retrieve_type,
    # which takes pokename as its parameter.
    pokename = str(input("Please enter your Pokémon: ").lower())
    pokerival = str(input("Please enter your rival's Pokémon: ").lower())
    user_types = [retrieve_type(pokename), retrieve_type(pokerival)]
    user_types = [user_types, pokename, pokerival]
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


def game(user1_type, user2_type):
    # user_types: list = (pokemon_signup()[0])
    relationsdict1 = find_type_relation(user1_type)
    pprint(relationsdict1)
    relationsdict2 = find_type_relation(user2_type)
    # print(user2_type)
    # pprint(relationsdict1['double_damage_to'])

    # Deciding if the rival's type is weak to the user's pokemon.
    #If re-using, might use and call from a function 
    def damage_calculator(user_type, relationsdict):
        '''
        If I decide to make the following 'for' loop into a function:
        '''
        ...
    for type in user2_type:
        if type in relationsdict1["double_damage_to"]:
            print(f"{users[1]} deals double damage.")
        if type in relationsdict1["half_damage_to"]:
            print(f"{users[1]} deals half damage.")
        if type in relationsdict1["no_damage_to"]:
            print(f"{users[1]} deals no damage.")
        if type in relationsdict1["quad_damage_to"]:
            print(f"{users[1]} deals 4x damage.")
        else: print(f"{users[1]} dealt usual damage.")


    # relationsdict2 = find_type_relation(user_type_2)
    # if user1_type in 
    # pprint(user_type_1, relationsdict1)
    # pprint(user_type_1, relationsdict2)
    # pprint(user_types)
    # pprint(relationsdict1)
    return relationsdict1


users: list = user_types
user1_type = users[0][0]
user2_type = users[0][1]

game(user1_type, user2_type)
