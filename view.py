import csv
file_name = "contacts.csv"

def view_contacts():
    with open("contacts.csv", "r") as file:
        contacts = csv.DictReader(file)

        print("---------------------------------------------------------------------------------------")
        for x in contacts:
            print(f"Name: {x['Name']} |  Email: {x['Email']} |  Phone Number: {x['Phone Number']} |  Address: {x['Address']}")
        print("---------------------------------------------------------------------------------------")
