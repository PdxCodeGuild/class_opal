relative_path = 'code/lizzie/python/lab11_files/contact_list.csv'

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


#CREPL is one big while loop with a menu
while True:
    # print(f'The contact list is: {contact_list}')
    user_response = input('''
What would you like to do:
add new contact
display contact info
update a contact
delete contact
or 'quit' to exit.
''')

    if user_response == 'quit':
        break

    #Add new contact.
    if user_response == 'add new contact':
        add_contact = input('''Please enter a name, fandom, and profession \
for the new contact or 'done' to quit: 
        ''')
        if add_contact == 'done':
            break
        else:
            add_list = add_contact.split(', ')
            new_contact = dict(zip(keys,add_list))
            contact_list.append(new_contact)
            # print(f"The contact list is now: {contact_list}.")


    # Retrieve a record.
    if user_response == 'display contact info':
        contact_name = input("Please provide the contact's name or \
'done' to quit: ")
        if contact_name == 'done':
            break
        if contact_name not in contact_list:
            print("Sorry! Invalid contact.")
        for contact_dict in contact_list:
            if contact_name == contact_dict['name']:
                print(f'Here is that contact: {contact_dict}.')


    # Update a record:
    if user_response == 'update a contact':
        contact_name = input("Please enter the contact's name or\
 'done' to quit: ")
        if contact_name == 'done':
            break
        if contact_name not in contact_list:
            print("Sorry! Invalid contact.")
        key_to_update = input("Please enter an attribute\
 (name, fandom, profession) to edit: ")
        new_attribute = input("Please enter the new attribute: ")
        for contact in contact_list:
            if contact["name"] == contact_name:
                if "fandom" == key_to_update:
                    contact["fandom"] = new_attribute
                elif "profession" == key_to_update:
                    contact["profession"] = new_attribute
                elif "name" == key_to_update:
                    contact["name"] = new_attribute


    #Delete a record.
    if user_response == 'delete contact':
        contact_name = input("Please enter the name of the contact \
you'd like to delete or 'done' to quit: ")
        if contact_name == 'done':
            break
        if contact_name not in contact_list:
            print("Sorry! Invalid contact.")
        for contact_dict in contact_list:
            if contact_name == contact_dict['name']:
                contact_list.remove(contact_dict)

contact_output = []

#Creating the headers
for x in contact_list:
    #retrieving the keys of the dicts (name, favorite food, age)
    headers = contact_list[0].keys()
header_line = ",".join(headers)
contact_output.append(header_line)


#converting the list of dictionaries into a list so it can be output into the csv file
for contact in contact_list:
    contact_info = [x for x in contact.values()]
    contact_line = ','.join(contact_info)
    contact_output.append(contact_line)

#prints everything but the header for the user, so they can view the contacts.
print(f"The contact list is now: {contact_output[1:]}.")

out_path = 'code/lizzie/python/lab11_files/new_contacts.csv'

output_content = '\n'.join(contact_output)

with open(out_path, 'w') as f:
    f.write(output_content)
