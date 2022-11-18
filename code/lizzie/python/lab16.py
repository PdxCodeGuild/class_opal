# Lab 16: Dad Joke API

# Use the [Dad Joke API](https://icanhazdadjoke.com/api) to get a dad joke and 
# display it to the user. You may want to also use [time.sleep](https://www.geeksforgeeks.org/sleep-in-python/) 
# to add suspense.

""" 

# importing the request library.
import requests

# ## Part 1

# Use the [requests](../docs/15%20Requests.md) library to send an HTTP request
#  to `https://icanhazdadjoke.com/` with the `accept` header as `application/json`. 
# This will return a dad joke in JSON format.


# These all do roughly the same thing
response = requests.get(
    'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})


#  You can then use the `.json()` method 
# # on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.


# Parse the text (JSON) response into a python dictionary
# response_text = json.loads(response.text)
response_text = response.json()


pprint(response_text)


# yikes = requests.get('https://icanhazdadjoke.com/')
# print(yikes.text)
 """


# ## Part 2

# Add the ability to "search" for jokes using [another endpoint](https://icanhazdadjoke.com/api#search-for-dad-jokes).
#  Create a REPL that allows one to enter a search term and go through jokes one at a time. 
# You can also add support for multiple pages.

""" while True:

    response = input("\nEnter a search term here or 'done' to quit: ")

    if response == 'done':
        print(f'You entered {numbers}.')
        print(f'The sum of the numbers is {sum(numbers)}')
        break """
