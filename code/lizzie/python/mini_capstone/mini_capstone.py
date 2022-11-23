""" 
mini capstone: Pokémon Face-Off 
"""
# User gives stats about their pokemon.
# How do we resolve not knowing what the enemy's info is?

# All we really need is user's pokemon name
# Make call to API to return info about that Pokemon
# Take that info and decide who the winner is with it.

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
    response_text = response.json()
    # Some pokemon have 2 types, so this loop iterates through
    # both slots and appends them to the list as strings.
    user_type = []
    for slot in response_text['types']:
        user_type.append(slot['type']['name'])
    return user_type


#TODO: Do I need to keep this? How useful is this going to be for me?
def pokemon_signup():
    '''
    Takes the input of a user's pokemon name and returns the types of that user's Pokémon.
    '''
    pokename1 = str(input("Please enter your Pokémon's name: ").lower())
    # user 1 is being assigned the list of types returned from retrieve_type,
    # which takes pokename1 as its parameter.
    user1_type: list = retrieve_type(pokename1)
    print(f"User 1's {pokename1} is a(n) {user1_type} type.")
    pokename2 = str(input("Please enter your Pokémon's name: ").lower())
    user2_type: list = retrieve_type(pokename2)
    print(f"User 2's {pokename2} is a(n) {user2_type} type.")
    return user1_type, user2_type


# pokemon_signup()


#TODO: How do you handle dual-type pokemon, where the list has two things in it?
# Have to parse the list and feed each one to the function.
# ANOTHER function to fun this function with each of the user types? Should pokemon_signup return
# strings instead?
def find_type_relation(user_type):
    '''
    Returns the relationship of the given type to all other types.
    Only does one type at a time.
    '''
    users_type = 'fire'
    url = f'https://pokeapi.co/api/v2/type/{users_type}/'

    response = requests.get(url)
    response_text = response.json()
    # pprint(response_text)

    pprint(response_text['damage_relations'])
    ...

users_type = 'fire'
url = f'https://pokeapi.co/api/v2/type/{users_type}/'

response = requests.get(url)
response_text = response.json()
# pprint(response_text)

# pprint(response_text['damage_relations']['double_damage_to'])
# pprint(response_text['damage_relations'])



pprint(response_text['damage_relations'])
print( '!' * 8)
pprint(response_text['damage_relations']['half_damage_to'])
print( '!' * 8)
pprint(response_text['damage_relations']['half_damage_to'][0])
print( '!' * 8)
pprint(response_text['damage_relations']['half_damage_to'][0]['name'])


# I went one too deep with all of this?
half_damage_to = []

for name in response_text['damage_relations']['half_damage_to']:
    half_damage_to.append([name][0]['name'])
    print(half_damage_to)


    # type_relation.append(damage[0])
    # type_relation.append(damage)
    # type_relation.append(response_text) 

""" #  for appending "double_damage_from", etc.
    for name in response_text['damage_relations']:
        type_relation.append(name)
        print(type_relation) """

# find_type_relation('steel')

#make another API call to retrieve what the heck happens
# with these two dudes.

# Pokemon (endpoint): retieving type
# Types (endpoint) will be a differnt API call.
    # TypeRelations (type)

#Gathering the two types