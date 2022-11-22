# Lab 17: Quote API

# Importing requests library
import requests
from pprint import pprint


# Nested while loops so if you don't want to view the next page of a certain entry,
# you break and return to the main introduction and can retry with different input.
# added a variable for a nested while loop to break completely out of both loops.
breaker = False
while True:
    # Introducing print variable that will increment by 1
    # Every time user inputs they want to see next page.
    page = 1
    print("""
    Welcome! This program will return 25 quotes associated with your chosen keyword.
    """)
    user_keyword = str(input('Please enter a keyword: '))
    url = 'https://favqs.com/api/quotes?'

    while True:
        # Have params inside while loop so it updates with new page number each time.
        params = {
            'page' : str(page),
            'filter' : user_keyword
        }
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        built_url = requests.get(url, params=params, headers=headers)
        quotes_info = built_url.json()

        print(f"Quotes associated with {user_keyword} - page {page}")
        for quote in quotes_info['quotes']:
            try:
                print(f"""
"{quote['body']}"\n —- {quote['author']}
                """)
            except KeyError:
                print("Sorry! You've hit the end of the list that uses those keywords.")
                # added a flag so I can break out of the while loop, too, otherwise
                # it prints unwanted statements.
                breaker = True
                break
        if breaker:
            break
        print(f"Page {page} for keyword '{user_keyword}.'")
        
        user_next_page = input("Would you like to see the next page? ")
        if user_next_page == 'yes' or user_next_page == 'y' or user_next_page == 'yeah' or user_next_page == 'next':
            page += 1
        else:
            break

