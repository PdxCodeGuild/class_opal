relative_path = 'my_contact.csv'

with open(relative_path, 'r') as file:
    contact_lines = file.read().split('\n')

keys = contact_lines[0].split(',')
contact_lines.pop(0)

contact_list = []


for i, contacts in enumerate(contact_lines):
    row = contact_lines[i].split(',')
    contact = dict(zip(keys,row)) 
    contact_list.append(contact)


while True:
    print(f'The contact list is: {contact_list}')
    user_response = input('''
Would you like to:
add new contact
display contact info
update a contact
delete contact
or 'quit' to exit.
''')

    if user_response == 'quit':
        break


    if user_response == 'add new contact':
        add_contact = input('''Please enter a name, favorite food, and favorite color \
for the new contact or 'done' to quit: 
        ''')
        if add_contact == 'done':
            break
        else:
            add_list = add_contact.split(', ')
            new_contact = dict(zip(keys,add_list))
            contact_list.append(new_contact)
            break
   
    if user_response == 'display contact info':
        contact_name = input("Please provide the contact's name or \
'done' to quit: ")
        if contact_name == 'done':
            break
        for contact_dict in contact_list:
            if contact_name == contact_dict['Name']:
                print(f'Here is that contact: {contact_dict}.')



    if user_response == 'update a contact':
        contact_name = input("Please enter the contact's name or\
 'done' to quit: ")
        if contact_name == 'done':
            break
        update_info = input("Please enter an attribute\
 (name, favorite food, favorite color) to edit: ")
        favorites = input("Please enter the new update: ")
        for contact in contact_list:
            if contact["Name"] == contact_name:
                if "Favorite food" == update_info:
                    contact["Favorite food"] = favorites
                elif "Favorite Color" == update_info:
                    contact["Favorite Color"] = favorites
                elif "Name" == update_info:
                    contact["Name"] = favorites


    
    if user_response == 'delete contact':
        contact_name = input("Please enter the name of the contact \
you'd like to delete or 'done' to quit: ")
        if contact_name == 'done':
            break
        if contact_name not in contact_list:
            print("Sorry! Invalid contact.")
        for contact_dict in contact_list:
            if contact_name == contact_dict['Name']:
                contact_list.remove(contact_dict)

contact_output = []


for x in contact_list:
    headers = contact_list[0].keys()
header_line = ",".join(headers)
contact_output.append(header_line)


for contact in contact_list:
    contact_info = [x for x in contact.values()]
    contact_line = ','.join(contact_info)
    contact_output.append(contact_line)


print(f"The contact list is now: {contact_output[1:]}.")

out_path = 'my_contact.csv'

output_content = '\n'.join(contact_output)

with open(out_path, 'w') as f:
    f.write(output_content)