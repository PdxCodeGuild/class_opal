import requests
from pprint import pprint
from os import system


def random_quote():
    response = requests.get(f'https://favqs.com/api/qotd')
    system('cls||clear')
    print(f'''
    {response.json()['quote']['body']}\n
    -{response.json()['quote']['author']}
    
    
    ''')
    while True:
        yes_or_no = input('Would you like to see another quote? yes or no: ')
        if yes_or_no == 'yes':
            random_quote()
        break
    return


def keyword_quotes(keyword='code', page=1):
    response = requests.get(
        f'https://favqs.com/api/quotes?page={str(page)}&filter={keyword}',
        headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    last_page = response.json()['last_page']
    quotes = response.json()['quotes']
    system('cls||clear')
    for quote in quotes:
        print(f'''
{quote['body']}\n
-{quote['author']}


''')
    if last_page:
        print(f'This is all of the quotes on {keyword}!')
        return
    else:
        while True:
            yes_or_no = input(
                'Would you like to see the next page of quotes? yes or no: ')
            if yes_or_no == 'yes':
                page += 1
                keyword_quotes(keyword, page)
            return


while __name__ == '__main__':
    print('Welcome to the Quote API!')
    while True:
        command = input(
            "Type 'random' to get a random quote, or 'search' to get a page of quotes about your keyword.")
        if command == 'random':
            random_quote()
            break
        elif command == 'search':
            keyword = input(
                'Type the keyword about which you would like to see quotes.')
            keyword_quotes(keyword)
            break
        else:
            print('That is an invalid input.')

    print('\n\n"Bye, Felicia!"\n-Craig')
    exit()
