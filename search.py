import csv
file_name = "contacts.csv"

print("CBMS -> SEARCH CONTACT")
search = input("Enter Searching Name:  ")

with open("contacts.csv", "r") as file:
    cont = csv.DictReader(file)

    for x in cont:
        if search in {x['Name']}:
            print(f"Name: {x['Name']}")
            print(f"Email: {x['Email']}")
            print(f"Phone Number: {x['Phone Number']}")
            print(f"Address: {x['Address']}")
        else:
            print("No Data Found!")