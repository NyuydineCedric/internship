def contact_menu(contacts):
    
    while True:

        name = input("Enter a name: ")

        

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found")


contacts = {
    "Cedric": "678772649",
    "Jey": "678273645",
    "Jimmy": "3473812723",
    "Solo": "4562738273",
    "Jim": "8978927672",
}

contact_menu(contacts)