import requests
import pprint

response = requests.get('https://icanhazdadjoke.com', headers= {'Accept': 'application/json'})

results = response.json()
#print(results)
#pprint.pprint(results)

user_input = input("Would you like to hear a joke? yes / no ")

if user_input == 'yes':
    print(results['joke'])
else:
    print("Too bad! You're missing out on a good one!")

