import csv
file_name = "contacts.csv"

def search_contact(search_name):
    found = False

    with open(file_name, "r") as file:
        contacts = csv.DictReader(file)

        for cont in contacts:
            if search_name.strip().lower() in cont['Name'].strip().lower():
                print(f"Name: {cont['Name']}")
                print(f"Email: {cont['Email']}")
                print(f"Phone Number: {cont['Phone Number']}")
                print(f"Address: {cont['Address']}")
                found = True

    if not found:
        print(f"{search_name}: Related No Data Found!")


