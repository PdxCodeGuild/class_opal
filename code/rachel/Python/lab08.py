from contextlib import ContextDecorator
import csv
"""Version 1: Build a program to manage a list of contacts. Build a CSV with names, colors, fruit; headers might consist of name, favorite fruit, favorite color. Open CSV, convert lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values. """
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    new_lists = [line.split(',') for line in lines] #turn those strings into their own list of things to work with: [['name', 'favorite color', 'favorite fruit'], ['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
    #print(new_lists)

headers = new_lists.pop(0) #pop out first list
#print(headers) #['name', 'favorite color', 'favorite fruit']
#print(new_lists) #[['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
"""Now we need a function that will pull each list out and then zip it to the first list in a loop / list comprehension. End result is a list of seperate dictionaries"""
def list_builder(funny, new_lists): #parameter names only apply to the function definition; they are simply placeholders
    local_list = []
    for list in new_lists:
        sing_dict = dict(zip(funny,list))
        local_list.append(sing_dict)
    return local_list
#print(list_builder(headers, new_lists)) #this is where I tell it to use the particular lists I want it to use
contact_list = list_builder(headers, new_lists)
#print(contact_list)

def update_record(contact_list, headers):
    user_name = input("Enter the user's name ")
    for contact in contact_list:
        if contact['name'] == user_name:
            for header in contact:
                # print(f'{header}: {contact[header]}')
                return contact

# def get_record(contact_list, headers):
#     header_string = "\n" + "\n".join(headers) + "\n"
#     key_input = input(f"What do you want to search by? Choose from: {header_string}")
#     value_input = input("What is your search term? ")
#     record = list(filter(lambda contact: contact[key_input] == value_input, contact_list))
#     return record


"""Version 2: Implement a CRUD REPL: 
Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered."""

while True:
    decision1 = input('Enter an option:\n To enter your contact information, enter "new user".\n To verify your information enter "verify".\n To update your record, enter "update".\n To delete your information, enter "delete".\n To quit the program, enter "quit". ')
    if decision1 == 'quit':
        print('Thanks for visiting')
        break
    elif decision1 == 'new user':
        user_name = input("Enter your first name: ")
        fav_color = input("Enter your favorite color: ")
        fav_fruit = input("Enter your favorite fruit: ")
        new_user = {
            'name': user_name,
            'favorite color': fav_color,
            'favorite fruit': fav_fruit
            }
        contact_list.append(new_user)
        print(new_user)
    #print(contact_list)
        """Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information"""


    elif decision1 == 'verify':
        user_name = input('To verify your information, enter your first name ')
        for contact in contact_list: #for each list in the file
            if contact['name'] == user_name: #find the name in the file
                for header in contact: 
                    print(f'{header}: {contact[header]}') #print out all the key value pairs in that list
        """Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set."""


    elif decision1 == 'update':
        #found_contact = get_record(contact_list, headers) #run function
        contact = update_record(contact_list, headers) #run function
        update_key = input(f'Which field do you want to update? {headers}') #ask user which key they want to update and provide the keys so they know what to choose
        update_value = input(f'Enter the correct information for {update_key}: ') #ask user what they want to change the value for that key to
        #found_contact[update_key] = update_value #update the record 
        contact[update_key] = update_value #update the record 
        #contact_list.append(match)
        #print(contact_list)
        """Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list."""


    elif decision1 == 'delete':
        contact = update_record(contact_list, headers)
        contact_list.remove(contact)
        print('Your record has been deleted')
    
    #print(contact_list)           

contact_csv_new = []
contact_csv_new.append(headers)
for contact in contact_list:
    contact_csv_new.append(list(contact.values()))
output_string = "\n".join([",".join(row) for row in contact_csv_new])
with open('contacts.csv', 'w') as file:
    file.write(output_string)


