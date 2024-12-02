import csv
file_name = "contacts.csv"
print("CBMS -> REMOVE CONTACT")

remove_data = input("Input the name to remove: ")

with open(file_name, "r") as file:
    cont = csv.reader(file)
    r_data = list(cont)


found = False
with open(file_name, "w", newline='') as file:
    remov = csv.writer(file)
    for x in r_data:
        if x[0] != remove_data:
            remov.writerow(r_data)
        else:
            found = True


if found:
    print(f"Name: {remove_data} removed successfully!")
else:
    print(f"{remove_data} : No Record Found!")
