import requests
import json
import pprint
"""Version 1: Get a random quote, parse the JSON in the response into a python dictionary, and show the quote and the author. """
#response = requests.get('https://favqs.com/api/qotd', headers= {'Content-Type': 'application/json'})
# results = response.json()
# response = requests.get('https://favqs.com/api/qotd', params={'format': 'json'}) #gtg
# print(response.text) #gtg
# data = response.json() #gtg
# #data = json.loads(response.text) #must use import json for this to work
# print(data['quote']['body']) #gtg
# print(data['quote']['author']) #gtg

"""Version 2: Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword."""
keyword = input("Enter a keyword to search for quotes: ")
print(f'25 quotes associated with {keyword}')
kw_response = requests.get(f'https://favqs.com/api/quotes?filter=+{keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
kw_quotes = kw_response.json()
quotes_list = kw_quotes['quotes'] #extracting the quotes dictionary from the json response
for quote in quotes_list:
    author = quote['author']
    body = quote['body']
    print(body, author)
def get_quote():
    for quote in quotes_list:
        author = quote['author']
        body = quote['body']
        return body, author
#pprint.pprint(quotes_list)
#pprint.pprint(kw_quotes) #green is class, yellow is method

while True:
    decision = input("Enter 'next page' to see more quotes, 'done' to select a new search term, or exit to exit ")
    if decision == 'exit':
        print('Thanks for visiting')
        break
    elif decision == 'done':
        keyword = input("Enter a keyword to search for quotes: ")
        for quote in quotes_list:
            author = quote['author']
            body = quote['body']
            print(body, author)
    elif decision == 'next page':
        if kw_quotes["last_page"] == False:
            print(f'25 more quotes associated with {keyword}')
            page = kw_quotes['page'] + 1
            kw_response = requests.get(f'https://favqs.com/api/quotes?page=+{page}&filter=+{keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            kw_quotes = kw_response.json()
            quotes_list = kw_quotes['quotes']
            for quote in quotes_list:
                author = quote['author']
                body = quote['body']
                print(body, author)
            #print(get_quote())
        #if kw_quotes["last_page"] == True:
        elif kw_quotes["last_page"] == True:
            print(f"Sorry, there aren't any more quotes associated with {keyword}")
            keyword = input("Enter a keyword to search for quotes or exit to exit ")
            if keyword == 'exit':
                print('Thanks for visiting')
                break
            else:
                for quote in quotes_list:
                    author = quote['author']
                    body = quote['body']
                    print(body, author)







