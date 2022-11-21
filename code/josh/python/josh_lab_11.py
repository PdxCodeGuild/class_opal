# Lab 11: Contact List
relative_path = 'class_opal\code\josh\python\contacts.csv'

# Opens file at 'relative_path' and converts lines into a list of strings
with open(relative_path, 'r') as file:
    lines:list = file.read().split('\n')

contacts = []
# Creates a list of strings, where each string will be used as a dictionary key from the first line in the file above
keys: list[str] = lines[0].split(',')  

# Iterates through the remaining list strings and converts each string to a dictionary value 
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
    
    
contacts_output = []

# Places keys from dictionary back into index '0' at the beginning of the list of lines from the file above
key_info = [k for k in contacts[0].keys()]
single_key = ','.join(key_info)
contacts_output.append(single_key)

# Places values from dictionary back into remaining indexes after '0' in the list of lines from the file above, including additional entries from program
for contact in contacts:
    contact_info = [c for c in contact.values()]
    single_contact = ','.join(contact_info)
    contacts_output.append(single_contact)

# Overwrites original file with information from 'contacts_ouput' list above 
output_path = 'class_opal\code\josh\python\contacts.csv'
output_content = '\n'.join(contacts_output)

with open(output_path, 'w') as file:
    file.write(output_content)