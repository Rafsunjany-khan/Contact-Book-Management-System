import csv
file_name = "contacts.csv"

def remove_contacts():
    remove_data = input("Input the name to remove: ")

    with open(file_name, "r") as file:
        contacts = csv.reader(file)
        r_data = list(contacts)

    found = False
    with open(file_name, "w", newline='') as file:
        remove = csv.writer(file)
        for data in r_data:
            if data[0] != remove_data:
                remove.writerow(data)
            else:
                found = True
    if found:
        print(f"Name: {remove_contacts} removed successfully!")
    else:
        print(f"{remove_data} : No Record Found!")

