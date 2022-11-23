# Python Mini-Capstone

# Your program needs to utilize an external library.  The functionality of the program is up to you.

# 0930 and 1330 Stand Ups to answer 3 questions:
    # What did you do in your last session?
    # What will you do in this session?
    # What roadblock do you have, if any?

# 5-minute (roughly) Presentations:
    # A demo of your project
    # A look at the code
    # Time for questions
    # There is more info on presentations in the README

######################################################################################################################################################
######################################################################################################################################################

import requests
import pandas as pd
# import json
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

# response = requests.get('https://taxfoundation.org/tax-burden-by-state-2022/#results')
# response = requests.get('https://files.taxfoundation.org/20220407173521/State-and-Local-Tax-Burdens-2022..pdf')
# response_text = response.json()
# pprint(response_text)
# author  = response_text['quote']['author']
# quote = response_text['quote']['body']

with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup = BeautifulSoup(response, 'html.parser')
    # for anchor in soup.find_all('table'):
        # print(anchor.get('td', ''))

# for caption in soup.find_all('caption'):
#     print(caption)

# for table in soup.find('table'):
#     print(table)

    # if table == 'Table 1':
    #     print(table)

    # State, Effective Tax Rate, Rank
print(soup.prettify)
# print(soup.state)
