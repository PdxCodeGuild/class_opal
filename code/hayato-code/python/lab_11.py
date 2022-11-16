relative_path = 'hayato-code\python\my_contact.csv'

with open(relative_path, 'r') as file:
    contact_lines = file.read().split('\n')

keys = contact_lines[0].split(',')
contact_lines.pop(0)

#Empty contact list to store contacts
contact_list = []

#enumerate so it loops through contact_lines for each index
for i, contacts in enumerate(contact_lines):
    #splitting each contact line into a list of strings
    row = contact_lines[i].split(',')
    contact = dict(zip(keys,row)) #attaches correct key to correct value
    contact_list.append(contact)


print(f'The contact list is: {contact_list}')
user_response = input('''
What would you like to do:
add new contact
display contact info
update a contact
delete contact
''')


#Add new contact.
while user_response == 'add new contact':
    add_contact = input('''
Please enter a name, favorite food, and age \
for the new contact or 'done' to quit: 
    ''')
    if add_contact == 'done':
        break
    else:
        add_list = add_contact.split(', ')
        new_contact = dict(zip(keys,add_list))
        contact_list.append(new_contact)


# Retrieve a record.
while user_response == 'display contact info':
    contact_name = input("Please provide the contact's name or \
'done' to quit: ")
    if contact_name == 'done':
        break
    for contact_dict in contact_list:
        if contact_name == contact_dict['name']:
            print(contact_dict)


# Update a record: ask the user for the contact's 
# name, then for which attribute of the user they'd 
# like to update and the value of the attribute they'd 
# like to set.
while user_response == 'update a contact':
    contact_name = input("Please enter the contact's name or 'done' to quit: ")
    if contact_name == 'done':
        break

    key_to_update = input("Please enter an attribute (name, \
favorite food, age) to edit: ")
    new_attribute = input("Please enter the new attribute: ")

    contact_list.append(new_contact)

    print(contact_list)
    for contact_dict in contact_list:
        if contact_name == i['name']:
            print(i)




        # add_list = add_contact.split(', ')
        # new_contact = dict(zip(keys,add_list))
        # contact_list.append(new_contact)


#Delete a record.
while user_response == 'delete contact':
    contact_name = input("Please enter the name of the contact \
you'd like to delete or 'done' to quit: ")
    if contact_name == 'done':
        break
    for contact_dict in contact_list:
        if contact_name == contact_dict['name']:
            contact_list.remove(contact_dict)
