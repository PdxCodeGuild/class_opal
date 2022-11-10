# open contacts file in data subfolder
with open('data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

# create headers and data lists from contacts lines
headers = lines[0].split(',')
data = []
for i in range(1,len(lines)):
    data.append(lines[i].split(','))

# construct contacts as list of dictionaries for each contact
contacts = []
for line in data:
    entry = {}
    for header in headers:
        entry[header] = line[headers.index(header)]
    contacts.append(entry)


def create_contact(contacts: list):
    name = input("Enter contact name: ")
    fruit = input("Enter contact's favorite fruit: ")
    color = input("Enter contact's favorite color: ")
    contacts.append({'name': name, 'favorite fruit': fruit, 'favorite color': color})


def retreive_contact(contacts: list):
    name = input("What contact's info do you want to see? ")
    for contact in contacts:
        if contact['name'] == name:
            print(contact)


def update_contact(contacts: list):
    name = input("What contact's info do you want to update? ")
    attribute = input(f"What attribute do you want to update for {name}? ")
    new_value = input(f"What is the new value of that attribute for {name}? ")
    for contact in contacts:
        if contact['name'] == name:
            contact[attribute] = new_value


def delete_contact(contacts: list):
    name = input("What contact's info do you want to delete? ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)


def crud_repl(contacts):
    while True:
        action = input("What function do you want to perform on contacts? (create, retreive, update, delete) ")
        if action == 'create':
            create_contact(contacts)
        elif action == 'retreive':
            retreive_contact(contacts)
        elif action == 'update':
            update_contact(contacts)
        else:
            delete_contact(contacts)
        
        continuation = input("Would you like to perform another function? (y/n) ")
        if continuation == 'y':
            continue
        else:
            break

crud_repl(contacts)

# initialize output list
output_list = []

# create header line
headers = [x for x in contacts[0].keys()]
header_line = ""
for header in headers:
    header_line += header + ','

header_line = header_line.rstrip(',')
output_list.append(header_line)

# create data rows
for contact in contacts:
    contact_line = ""
    for key in contact.keys():
        contact_line += contact[key] + ','
    contact_line = contact_line.rstrip(',')
    output_list.append(contact_line)

# write updated contacts to file
out_path = 'data/contacts.csv'
output_content = '\n'.join(output_list)

with open(out_path, 'w') as f:
    f.write(output_content)