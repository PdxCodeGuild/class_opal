# Python Mini-Capstone: Build a program that solves a problem or accomplishes a task.

# Your program needs to utilize an external library (something that you pip install, browse https://awesome-python.com).
# The functionality of the program is up to you (get creative, solve an actual problem).

# 0930 and 1330 Stand Ups to answer 3 questions:
    # What did you do in your last session?
    # What will you do in this session?
    # What roadblock do you have, if any?

# Presentations:
# The presentations should be about 5 minutes long and include:
    # A demo of your project
    # A look at the code
    # Time for questions
    # There is more info on presentations in the README

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = requests.get('https://taxfoundation.org/tax-burden-by-state-2022/#results')
response_text = response.json()
pprint(response_text)
# author  = response_text['quote']['author']
# quote = response_text['quote']['body']

# with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))