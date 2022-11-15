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
    user_input = [name, state, branch]
    new_contact = dict(zip(keys, user_input))
    contacts.append(new_contact)
    retrieve = input('Enter a name to retrieve the record or \'q\' to exit: ')
    if retrieve == 'q':
        break
    else:
        for contact in contacts:
            if contact['name'] == retrieve:
                print(contact)
                break
            else:
                pass
        pass
            # elif retrieve not in contacts[0:]:
            #     print(f'\'{retrieve}\' is not in list of contacts.')
            #     break
    update = input('Enter a name to update a contact or \'q\' to exit: ')
    if update == 'q':
        break
    else:
        for contact in contacts:
            if contact['name'] == update:
                old_value = input('Enter the item to update (\'name\', \'state\', \'branch\'): ')
                new_value = input(f'Enter new value for {old_value}: ')
                contact[old_value] = new_value
                print(contact)
                break
            else:
            #     print(f'\'{retrieve}\' is not in list of contacts.')
                pass
    delete = input('Enter a name to delete a contact or \'q\' to exit: ')
    if delete == 'q':
        break
    else:
        for contact in contacts:
            if contact['name'] == delete:
                del contact
                print(contacts)
                break
            else:
                pass
       #print(contacts)

    # print(contacts)


# # Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


# # Step 3
# # When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't 
# # write it correctly the first time.