''' 
URL - Uniform Resource Locator

https://mail.google.com/u/0/#inbox

[protocol]://[*subdomain].[domain].[extension/TLD]/*path/to/wherever?query_parameters=extra_info

when you hit a url in your browser (or with the requests library, etc)
- your ISP sends it to your DNS (Domain Name Server)(the address book of the internet)
- the DNS resolves it into an IP address
- a request is sent to that address
- whoever is on the other end interprets the request and sends a response
- the response comes back in more or less the same way it went
- then the response can be interpreted by you 
    (your browser reading the html/css/JS, or you parsing the json, etc)
'''

import requests
from pprint import pprint
import json


parameters = {
    'results': '10',
    'nat': 'US',
    # 'seed': 'Kyle the Honey Badger',
    'inc': 'name,nat'
}

# These all do roughly the same thing
response = requests.get('https://randomuser.me/api/?results=10&nat=UA')
response = requests.get(
    'https://randomuser.me/api/', params={'results': '10', 'nat': 'IR'})
response = requests.get(
    'https://randomuser.me/api/', params=parameters, headers={'accept': 'application/json'})

print(response.url)
print(response.status_code)
print(response.encoding)
# print(response.text)

# Parse the text (JSON) response into a python dictionary
# response_text = json.loads(response.text)
response_text = response.json()


pprint(response_text)


# yikes = requests.get('https://api.kanye.rest')
# print(yikes.text)
