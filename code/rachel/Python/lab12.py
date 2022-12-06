import dlib #machine learning algorithms toolkit
import face_recognition
#import csv
import os #interact w/ the operating system
from os import listdir #gets the list of all files & directories in the current working directory 

"""Do I Know You?"""

'''STEP 1'''''''''
"""Compare an unknown person's picture against a known"""

# known_image = face_recognition.load_image_file("people_I_know/sandy_harris.jpeg")

# known_image_encoding = face_recognition.face_encodings(known_image)[0] #index 0 indicates first encoding / image of face

# '''STEP 1.a'''''''''
# #unknown_image = known_image = face_recognition.load_image_file("Unknown/tiger_lady_wannabe.jpeg") #unknown person test

# '''STEP 1.b'''''''''
# unknown_image = known_image = face_recognition.load_image_file("Unknown/unknown_sandy.jpeg")
# unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

# compare_images = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)

# if compare_images[0] == True:
#     print(f"You know them!")
# else:
#     print("This isn't the person you're looking for.")


'''STEP 2'''''''''
"""Compare one photo to all the images in a folder"""

'''STEP 2.a'''''''''
unknown_image = known_image = face_recognition.load_image_file("Unknown/tiger_lady_wannabe.jpeg") #unknown person test

'''STEP 2.b'''''''''
#unknown_image = known_image = face_recognition.load_image_file("Unknown/unknown_sandy.jpeg")
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

directory = 'people_I_know' 

for file in [file for file in os.listdir(directory) if ".jpeg" in file]:
    known_image = face_recognition.load_image_file(f"{directory}/{file}")
    known_image_encoding = face_recognition.face_encodings(known_image)[0] #index 0 indicates first encoding / image of face
    compare_images = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)
    if compare_images[0] == True:
        print(f"You know them! Their name is {file.rpartition('.')[0]}.")#print the filename w/o the extension
        break #stop once the True condition is met
    else:
        print("This isn't the person you're looking for.")
    #print(file)


'''STEP 3'''''''''
# """Using function and while loop so that if the photo doesn't find a match, there's only 1 output saying so"""
# def compare():
#     for file in [file for file in os.listdir(directory) if ".jpeg" in file]:
#         known_image = face_recognition.load_image_file(f"{directory}/{file}")
#         known_image_encoding = face_recognition.face_encodings(known_image)[0]
#         compare_images = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)
#         if compare_images[0] == True:
#             print (f"You know them! Their name is {file.rpartition('.')[0]}.")
#             return True
# #print(compare())
# while compare() == False:
#     print("This person is not in your contacts.") #when false, won't output anything


'''STEP 4'''''''''
"""This also works for images with multiple people"""

# sandy_harris = face_recognition.load_image_file("people_I_know/sandy_harris.jpeg")
# unknown_image = face_recognition.load_image_file("Unknown/Unknown5.jpeg")
# known_image_encoding = face_recognition.face_encodings(sandy_harris)[0]
# unknown_image_encoding = face_recognition.face_encodings(unknown_image)
# compare_images = face_recognition.compare_faces(known_image_encoding, unknown_image_encoding)

# unknown_image_file = "/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python/people_I_know/sandy_harris.jpeg"
# if compare_images[0] == True:
#     print("You know them!")
# else:
#     add_to_file = input("This person is not in your address book; do you want to add them? Y/N ")
#     if add_to_file == "Y":
#         name = input("Name: ")
#         contact_info = input("Contact info: ")
#         friends = input("Friends: ")
#         notes = input("Notes: ")
#         with open('address_book.csv', mode='w') as f:
#             fieldnames = ['name', 'contact_info', 'friends', 'notes', 'photos']
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerow({'name': name, 'contact_info': contact_info, 'friends': friends, 'notes': notes, 'photos': unknown_image_file})
#     else:
#         print("Maybe next time")

