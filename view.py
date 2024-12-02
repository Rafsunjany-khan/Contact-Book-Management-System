import csv
file_name = "contacts.csv"
print("CBMS -> VIEW ALL CONTACTS")

with open("contacts.csv", "r") as file:
    cont = csv.DictReader(file)
    for x in cont:
        print(f"Name: {x['Name']}")
        print(f"Email: {x['Email']}")
        print(f"Phone Number: {x['Phone Number']}")
        print(f"Address: {x['Address']}")
        print("---------------------------------------")