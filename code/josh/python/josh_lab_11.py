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


# CRUD REPL
while True:
    name = input('Enter a new name or type \'q\' to exit: ')
    if name == 'q':
        break
    state = input('Enter a new state abbreviation: ')
    branch = input('Enter a new military service abbreviation: ')
    user_input = [name, state, branch]
    new_contact = dict(zip(keys, user_input))
    contacts.append(new_contact)
    retrieve = input('Enter a name to retrieve the record or \'n\' to continue: ')
    if retrieve == 'n':
        pass
    else:
        for contact in contacts:
            if contact['name'] == retrieve:
                print(contact)
                break
            else:
                pass
        pass
    update = input('Enter a name to update a contact or \'n\' to continue: ')
    if update == 'n':
        pass
    else:
        for contact in contacts:
            if contact['name'] == update:
                old_value = input('Enter the item to update (\'name\', \'state\', \'branch\'): ')
                new_value = input(f'Enter new value for {old_value}: ')
                contact[old_value] = new_value
                print(contact)
                break
            else:
                pass
    delete = input('Enter a name to delete a contact or \'n\' to continue: ')
    if delete == 'n':
        pass
    else:
        for i, contact in enumerate(contacts):
            if contact['name'] == delete:
                contacts.pop(i)
                break
            else:
                pass
    
    
# Step 3 - Write the updated contact info to the CSV file to be saved
contacts_output = []

key_info = [k for k in contacts[0].keys()]
single_key = ','.join(key_info)
contacts_output.append(single_key)

for contact in contacts:
    contact_info = [c for c in contact.values()]
    single_contact = ','.join(contact_info)
    contacts_output.append(single_contact)

output_path = 'class_opal\code\josh\python\contacts.csv'
output_content = '\n'.join(contacts_output)

with open(output_path, 'w') as file:
    file.write(output_content)