with open('contacts.csv', 'r') as file:
    columns = file.readline()
    keys = columns.strip("\n").split(",")
    number_of_rows = len(keys) #get variable for number of rows for looping?
    contacts_list_of_dicts = [] #final answer
    contacts = file.readlines() #splits the rest of the contacts by line
    rows_list = []
    for row in contacts:
        rows_list.append(row.split(","))
    file.close()
    for item in rows_list:
        row_dict = {}
        for i in range(number_of_rows):
            row_dict[keys[i]] = item[i].rstrip("\n")
        contacts_list_of_dicts.append(row_dict)

    def new_contact():
        new_user_info = {} #Where to put new user info
        new_name = input("Enter new contact's name: ")
        new_user_info.update({'name': new_name}) #add name to list
        
        new_fruit = input("Enter new contact's favorite fruit: ")
        new_user_info.update({'favorite fruit': new_fruit}) #add fruit to list
        
        new_color = input("Enter new contact's favorite color: ")
        new_user_info.update({'favorite color': new_color}) #add color to list        
        contacts_list_of_dicts.append(new_user_info)
        output_content = list(new_user_info.values())
            
        with open('contacts.csv', 'a') as f:
            f.write(f'\n{",".join(output_content)}')
        print("Contact has been added")

    def retrieve_record():
        search_name = input("enter name to look up: ")
        for name in contacts_list_of_dicts:
            if name["name"] == search_name:
                print(name['name'], name['favorite fruit'], name['favorite color'])                
    def update_record():
        contact_name = input("enter name to update: ")        
        for contact in contacts_list_of_dicts:
            if contact["name"] == contact_name:
                attribute_to_update = input("What would you like to update? Favorite fruit, or favorite color? ")
                if attribute_to_update == "favorite fruit":
                    new_value = input("What is the new value? ")
                    contact['favorite fruit'] = new_value
                    print(contact['name'], contact['favorite fruit'], contact['favorite color'])      
                    with open('contacts.csv', 'w') as f:
                        contacts_list_of_dicts.insert(0, {'name':'name', 'favorite fruit':'favorite fruit', 'favorite color':'favorite color'})
                        for i, item in enumerate(contacts_list_of_dicts):
                            if contacts_list_of_dicts[i] == contacts_list_of_dicts[-1]:
                                f.write(f'{",".join(item.values())}')
                            else:
                                f.write(f'{",".join(item.values())}\n')   
                elif attribute_to_update == "favorite color":
                    new_value = input("What is the new value? ")
                    contact["favorite color"] =  new_value
                    print(contact['name'], contact['favorite fruit'], contact['favorite color'])      

                    with open('contacts.csv', 'w') as f:
                        contacts_list_of_dicts.insert(0, {'name':'name', 'favorite fruit':'favorite fruit', 'favorite color':'favorite color'})
                        for i, item in enumerate(contacts_list_of_dicts):
                            if contacts_list_of_dicts[i] == contacts_list_of_dicts[-1]:
                                f.write(f'{",".join(item.values())}')
                            else:
                                f.write(f'{",".join(item.values())}\n') 
    def delete_record():
        name = input("enter name of contact to DELETE: ")
        for contact in contacts_list_of_dicts:
            if contact['name'] == name:
                contacts_list_of_dicts.remove(contact)
                with open('contacts.csv', 'w') as f:
                    contacts_list_of_dicts.insert(0, {'name':'name', 'favorite fruit':'favorite fruit', 'favorite color':'favorite color'})
                    for i, item in enumerate(contacts_list_of_dicts):
                        if contacts_list_of_dicts[i] == contacts_list_of_dicts[-1]:
                            f.write(f'{",".join(item.values())}')
                        else:
                            f.write(f'{",".join(item.values())}\n')
        print("Contact has been deleted")
while True:
    choice = input("What would you like to do? Type 'add new user', 'retrieve', 'update', or 'delete' : ")
    if choice == 'add new user':
        new_contact()
    elif choice == 'retrieve':
        retrieve_record()
    elif choice == 'update':
        update_record()
    elif choice == 'delete':
        delete_record()



                

