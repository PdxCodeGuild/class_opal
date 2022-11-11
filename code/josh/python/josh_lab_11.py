# Lab 11: Contact List
relative_path = 'class_opal\code\josh\python\contacts.csv'

with open(relative_path, 'r') as file:
    lines:list = file.read().split('\n')

contacts = []
contact_dict = {}

keys: list[str] = lines[0].split(',')  

for line in lines[1:]:
    values: list[str] = line.split(',')
    for key in keys:
        contact_dict[key] = None
        for value in values:
            contact_dict[key] = value

    # for value in values:
    #     contact_dict[key] = value

print(contact_dict)

# for line in lines[1:]:
#     values: list[str] = line.split(',')
#     for key in keys:
#         for value in values:
#             if key not in contact_dict:
#                 contact_dict[key] = value


# for line in lines[1:]:
#     values = line.split(',')
#     print(values)

# Create a dictionary for each key:value pair in keys and values.
# Append dictionary to empty list 'contacts'


# Convert the list of strings into a list of dictionaries with one dictionary per user. 
# The text in the header represents the keys, the text in the other lines represent the values.

# Once you've processed the file, your list of contacts will look something like this...

# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]


# Step 2 - Implement a CRUD REPL
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


# Step 3
# When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't 
# write it correctly the first time.