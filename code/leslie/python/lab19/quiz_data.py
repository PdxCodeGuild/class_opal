import requests
import time

# my_params = {
#     "amount": 3,
#     "type": "multiple"
# }

# response = requests.get(
#     url="https://opentdb.com/api.php?amount=5&category=11&difficulty=medium&type=multiple", params=my_params)
# question_data = response.json()["results"]


num_of_questions_input = int(input(
    "\nGreetings, player! How many questions would you like in your game -- 5 or 10? "))

if num_of_questions_input != 5 and num_of_questions_input != 10:
    num_of_questions_input = 5
    print("\nYeah that wasn't an option, weirdo. You're getting 5 questions...")
my_params = {
    "amount": num_of_questions_input,
    "type": "multiple"
}
# time.sleep(3)
player_category_input = input(f"""

{num_of_questions_input} question it is! Please choose your category:

Movies  Music  TV  Cartoons  Video Games

Celebrities  History  General Knowledge

What category would you like?: """).lower()

if player_category_input == 'movies':
    print("\nMovies! Good choice! Here ya go!\n")
    response = requests.get(
        url="https://opentdb.com/api.php?amount=5&category=11&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == 'music':
    print("\nMusic! Excellent choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=12&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == 'tv':
    print("\nTV! Excellent choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=14&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == 'video games':
    print("\nVideo games! Good choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=15&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == 'celebrities':
    print("\nOoh--celebrities! Excellent choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=26&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == "history":
    print("\nHistory! Good choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=23&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == 'cartoons':
    print("\nCartoons! Excellent choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=32&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]

elif player_category_input == "general knowledge":
    print("\nGeneral knowledge! Excellent choice-- good luck!\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]
else:
    print("\nInvalid or unfunny choice, chief. You get general knowledge whether you like it or not.\n")
    response = requests.get(
        "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple", params=my_params)
    question_data = response.json()["results"]
