from os import system
relative_path = 'code/nick/python/lab11/contacts.csv'


MENU = """
Type 'create' to add a new contact. 
Type 'view' to retrieve and view an existing contact.
Type 'update' to update an existing contact.
Type 'delete' to delete an existing contact.
Or type 'done' to finish.
"""


def crud():
    acceptable_input = ['create', 'view', 'update', 'delete', 'done']
    contacts, headers = unpack_contacts(relative_path)
    names = '\n'.join([c['name'] for c in contacts])

    while True:
        print(names)  # I wouldn't do this, just for UX reasons
        command = input(MENU).lower()
        if command in acceptable_input:
            break
        else:
            print('That is an invalid input.')

    match command:
        case 'create':
            create_contact(contacts, headers)
            crud()
        case 'view':
            view_contact(contacts, command)
            crud()
        case 'update':
            update_contact(contacts, headers, command)
            crud()
        case 'delete':
            delete_contact(contacts, headers, command)
            crud()
        case 'done':
            system('cls||clear')
            print('Thank you, goodbye!')


def unpack_contacts(path=relative_path):
    '''
    unpack the CSV of contacts into a a dictionary
    '''
    with open(path) as file:
        contacts = file.read()

    # remove the headers from the data and store them where we can work with them separately
    contacts_lines: list = contacts.split('\n')
    headers = contacts_lines.pop(0).split(',')

    contacts = []
    for line in contacts_lines:
        line = line.split(',')
        contact_dict = {headers[i]: line[i] for i in range(len(headers))}
        # another version of the same thing
        # contact_dict = {header: line[i] for i, header in enumerate(headers)}
        contacts.append(contact_dict)

    return contacts, headers


def pack_contacts(contacts, headers, path=relative_path):
    '''
    packs the contacts dictionary back into a properly formatted CSV file
    '''
    headers = ','.join(headers)
    contact_lines = [','.join(c.values()) for c in contacts]

    contact_lines.insert(0, headers)
    contacts = '\n'.join(contact_lines)

    with open(path, 'w') as file:
        file.write(contacts)

    system('cls||clear')
    print('Changes committed.\n\n')


def retrieve_contact(contacts, command='view') -> dict:
    '''
    return a contact dictionary given the name of a contact from the user
    '''
    name = input(f'''  
Enter the name which you would like to {command} from the list above.
:''')
    for i, contact in enumerate(contacts):
        if name in contact.values():
            return contacts[i]


def create_contact(contacts: list[dict], headers: list[str]):
    '''
    create a new contact with all info and save it to the CSV
    '''
    new_contact = {}
    for header in headers:
        new_contact[header] = input(f"Enter the contact's {header}:  ")

    contacts.append(new_contact)
    pack_contacts(contacts, headers, relative_path)


def view_contact(contacts: list[dict], command: str):
    '''
    View a contact given a name from the user. 
    Give the option to delete, update, or go back to the main menu
    '''
    contact: dict = retrieve_contact(contacts, command)
    system('cls||clear')
    for key, val in contact.items():
        print(f'{key}: {val}')

    print('\n\n')


def update_contact(contacts: list[dict], headers: list[str], command: str):
    contact: dict = retrieve_contact(contacts, command)
    contacts.remove(contact)

    print('Type the key you would like to update from the following list.\n')
    for key in contact.keys():
        print(key)
    key_to_update = input('\n:  ')
    new_value = input('Type the new value:  ')
    contact[key_to_update] = new_value
    contacts.append(contact)

    pack_contacts(contacts, headers, relative_path)


def delete_contact(contacts: list[dict], headers: list[str], command: str):
    '''
    deletes a contact that is already selected
    '''
    contact: dict = retrieve_contact(contacts, command)
    for i, record in enumerate(contacts):
        if contact == record:
            contacts.remove(contacts[i])

    pack_contacts(contacts, headers, relative_path)


print('Welcome to the contact manager!')
crud()
