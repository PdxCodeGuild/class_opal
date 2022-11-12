from os import system
relative_path = 'class_opal/code/nick/python/lab11/contacts.csv'
relative_path2 = 'class_opal/code/nick/python/lab11/contacts_practice.csv'


def unpack_contacts(path=relative_path):
    '''
    unpack the CSV of contacts into a a dictionary
    '''
    with open(path) as file:
        contacts = file.read()

    # remove the headers from the data and store them where we can work with them separately
    contacts_lines: list = contacts.split('\n')
    contacts_headers = contacts_lines.pop(0).split(',')
    #establish contacts list
    contacts = []
    
    for line in contacts_lines:
        line = line.split(',')
        dict = {}
        for i, header in enumerate(contacts_headers):
            dict[header] = line[i]
        contacts.append(dict)

    return contacts, contacts_headers


def pack_contacts(contacts, headers, path=relative_path2):
    '''
    packs the contacts dictionary back into a properly formatted CSV file
    '''
    contacts = contacts
    headers = ','.join(headers)
    contact_lines = []
    for contact in contacts:
        contact_line = []
        for header in contact:
            contact_line.append(contact[header])
        contact_lines.append(','.join(contact_line))

    contact_lines.insert(0, headers)
    contacts = '\n'.join(contact_lines)

    with open(path, 'w') as file:
        file.write(contacts)

    print('Changes committed.')
        
        

def create_contact(unpacked_contacts = unpack_contacts(relative_path2)):
    '''
    create a new contact with all info an save it to the CSV
    '''
    headers = unpacked_contacts[1]
    contacts = unpacked_contacts[0]
    new_contact = {}
    for header in headers:
        new_contact[header] = input(f"Enter the contact's {header}:  ")

    contacts.append(new_contact)
    pack_contacts(contacts, headers, relative_path2)
    

def retrieve_contact(unpacked_contacts = unpack_contacts(relative_path2), command='view'):
    '''
    return a contact dictionary given the name of a contact from the user
    '''
    contacts = unpacked_contacts[0]
    headers = unpacked_contacts[1]
    names = []
    for contact in contacts:
        names.append(contact['name'])
    names = '\n'.join(names)
    name = input(f'''
Enter the name which you would like to {command} from the following list.
{names}

:''')
    for i, contact in enumerate(contacts):
        if name in contact.values():
            return contacts[i], contacts, headers


def view_contact(command='view'):
    '''
    View a contact given a name from the user. 
    Give the option to delete, update, or go back to the main menu
    '''
    contact, contacts, headers = retrieve_contact(unpack_contacts(relative_path2), command)
    # print(contact)
    system('cls||clear')
    for key, val in contact.items():
        print(f'{key}: {val}')

    command = input(f"""
If you are done with this contact, type 'done' to go back to the main menu.
If you would like to update or delete this contact, type 'update' or 'delete'
"""
)
    if command == 'update':
        update_contact(contact, contacts, headers, command)


def update_contact(contact, contacts, headers, command='update'):
    contacts = contacts
    headers = headers
    contact = contact
    for i, record in enumerate(contacts):
        if contact == record:
            contact = contacts.pop(i)

    print('Type the key you would like to update from the following list.')
    for key in contact.keys():
        print(key)
    key_to_update = input('\n:  ')
    new_value = input('Type the new value:  ')
    contact[key_to_update] = new_value
    contacts.append(contact)

    pack_contacts(contacts, headers, relative_path2)



    



# create_contact() #test
# print(unpack_contacts()) #test
# pack_contacts() #test
# retrieve_contact() #test
view_contact() #test
# update_contact()

