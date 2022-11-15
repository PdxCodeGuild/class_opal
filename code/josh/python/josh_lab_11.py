# Lab 11: Contact List
relative_path = 'class_opal\code\josh\python\contacts.csv'

with open(relative_path, 'r') as file:
    lines:list = file.read().split('\n')

contacts = []

keys: list[str] = lines[0].split(',')  

for line in lines[1:]:
    contact_dict = {}
    values: list[str] = line.split(',')
    for i, key in enumerate(keys):
        contact_dict[key] = values[i]
    contacts.append(contact_dict)

# Step 2 - Implement a CRUD REPL

while True:
    name = input('Enter a new name or type \'q\' to exit: ')
    if name == 'q':
        break
    state = input('Enter a new state abbreviation: ')
    branch = input('Enter a new military service abbreviation: ')
    new_contact = [name, state, branch]
    # contact_dict.update(new_contact)
    for i, key in enumerate(keys):
        contact_dict[key] = new_contact[i]######### Currently replacing last dictionary in list instead of adding new dictionary to end of list ###########
    # contacts.append(contact_dict)

    # for user_entry in new_contact:
    #     contact_dict[0] = name
    #     contact_dict[1] = state
    #     contact_dict[2] = branch
    #     # i, key in enumerate(keys):
    #     # contact_dict[key] = new_contact[i]
    # contacts.append(new_contact)
    
    print(contacts)

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


# Step 3
# When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't 
# write it correctly the first time.