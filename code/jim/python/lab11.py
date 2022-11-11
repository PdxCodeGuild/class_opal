# open contacts file in data subfolder
with open('data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

# create headers and data lists from contacts lines
headers = lines[0].split(',')
data = [lines[i].split(',') for i in range(1, len(lines))]

# construct contacts as list of dictionaries for each contact
contacts = []
for line in data:
    entry = {}
    for header in headers:
        entry[header] = line[headers.index(header)]
    contacts.append(entry)


def create_contact(contacts: list, name=""):
    """Add a contact to the database."""
    while True:
        if name == "":
            name = input("Enter contact name: ").lower()
        
        if name not in [contact['name'] for contact in contacts]:
            fruit = input(f"Enter {name.title()}'s favorite fruit: ")
            color = input(f"Enter {name.title()}'s favorite color: ")
            contacts.append({'name': name, 'favorite fruit': fruit, 'favorite color': color})
            print("Contact was created.")
            break
        else:
            while True:
                answer = input("That contact already exists in the database. Try again? (y/n) ").lower()
                if answer == 'y':
                    break
                elif answer == 'n':
                    return None
                else:
                    print("Please choose a valid response.")

def retreive_contact(contacts: list):
    """Retreive contact info from the database."""
    while True:
        name = input("What contact's info do you want to see? ").lower()
        if name in [contact['name'] for contact in contacts]:
            for contact in contacts:
                if contact['name'] == name:
                    print(f"{contact['name'].title()}'s favorite fruit is {contact['favorite fruit']} and their favorite color is {contact['favorite color']}")
                    return None
        else:
            while True:
                answer = input(f"{name.title()} is not in the database. Would you like to add them? (y/n) ").lower()
                if answer == 'y':
                        create_contact(contacts, name)
                        return None
                elif answer == 'n':
                    return None
                else:
                    print("Please choose a valid response.")

def update_contact(contacts: list):
    """Update an attribute for a contact in the database."""
    while True:
        name = input("What contact's info do you want to update? ").lower()
        if name in [contact['name'] for contact in contacts]:
            while True:
                attribute = input(f"What attribute do you want to update for {name.title()}? ('favorite fruit' or 'favorite color') ").lower()
                if attribute in ['favorite fruit', 'favorite color']:
                    new_value = input(f"What is {name.title()}'s {attribute}? ")
                    for contact in contacts:
                        if contact['name'] == name:
                            contact[attribute] = new_value
                            return None
                else:
                    print(f"{attribute.title()} is not a valid attribute in the database.")
                
        else:
            while True:
                answer = input(f"{name.title()} is not in the database. Would you like to add them? (y/n) ").lower()
                if answer == 'y':
                        create_contact(contacts, name)
                        return None
                elif answer == 'n':
                    return None
                else:
                    print("Please choose a valid response.")

def delete_contact(contacts: list):
    """Delete a contact from the database."""
    name = input("What contact's info do you want to delete? ").lower()
    if name in [contact['name'] for contact in contacts]:
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
    else:
        while True:
            answer = input(f"{name.title()} is not in the database. Would you like choose another contact? (y/n) ").lower()
            if answer == 'y':
                    delete_contact(contacts)
                    return None
            elif answer == 'n':
                return None
            else:
                print("Please choose a valid response.")

def crud_repl(contacts):
    while True:
        action = input("What function do you want to perform on contacts? (Create, Retreive, Update, Delete, None) ").lower()
        if action == 'create':
            create_contact(contacts)
        elif action == 'retreive':
            retreive_contact(contacts)
        elif action == 'update':
            update_contact(contacts)
        elif action == 'delete':
            delete_contact(contacts)
        elif action == 'none':
            break
        else:
            print("Please choose a valid response.")

        continuation = input("Would you like to perform another function? (y/n) ")
        if continuation == 'y':
            continue
        else:
            break

crud_repl(contacts)

print(contacts)

# initialize output list
output_list = []

# create header line
headers = [x for x in contacts[0].keys()]
header_line = ",".join(headers)
output_list.append(header_line)

# create data rows
for contact in contacts:
    contact_data = [x for x in contact.values()]
    contact_line = ",".join(contact_data)
    output_list.append(contact_line)

# write updated contacts to file
out_path = 'data/contacts.csv'
output_content = '\n'.join(output_list)

with open(out_path, 'w') as f:
    f.write(output_content)