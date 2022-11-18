# Lab 16: Dad Joke API

import requests


#keeping everything in one loop.
while True:

    user_response = str(input("\nEnter a search term here or 'quit' to quit: "))
    
    if user_response == "quit" or user_response == "clear":
        print(f'\nHow do you say goodbye to your two sons?\nBison.')
        break

    parameters = {
        'term': user_response
    }
    response = requests.get(
        'https://icanhazdadjoke.com/search', params=parameters, headers={'accept': 'application/json'})
    response_text = response.json()

    # Telling the user how many jokes there are so they know how many to expect if they
    # choose to sort through them. Also works well if no jokes are returned.
    print(f"There are {response_text['total_jokes']} total joke(s) with this search term.")

    if user_response != "quit":
        #Accessing the list of dicts inside 'results'
        for dict in (response_text['results']):
            #Acessing the key 'joke' inside the dict
            print(dict['joke'])
            next_joke_query = input("Would you like to see the next joke? y or n: ")
            # The for loop will continue showing the next joke if the responses are affirmative
            # Or repeat the search term the user was inputting earlier.
            if next_joke_query == 'y' or next_joke_query == 'yes' or next_joke_query == user_response:
                continue
            elif next_joke_query == 'n' or next_joke_query == 'no':
                print("\nI decided to quit my job as a personal trainer because\
I'm not big enough or strong enough.\nI've handed in my Too Weak notice.")
                break
            else:
                break
