import requests
from pprint import pprint

breaker = False
while True:
    page = 1
    print("""
    Run this program to look for specific keywords of your choice.
    """)
    user_keyword = str(input('Please enter a keyword: '))
    url = 'https://favqs.com/api/quotes?'

    while True:
        params = {
            'page' : str(page),
            'filter' : user_keyword
        }
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        proper_url = requests.get(url, params=params, headers=headers)
        quotes_info = proper_url.json()

        print(f"Quotes associated with {user_keyword} - page {page}")
        for quote in quotes_info['quotes']:
            try:
                print(f"""
                "{quote['body']}"\n —- {quote['author']}
                """)
            except KeyError:
                print("That is all that we have for you! ")
                breaker = True
                break
        if breaker:
            break
        print(f"Page {page} for keyword '{user_keyword}.'")
        
        user_next_page = input("Would you like to see the next page? ")
        if user_next_page == 'yes' or user_next_page == 'next':
            page += 1
        else:
            break