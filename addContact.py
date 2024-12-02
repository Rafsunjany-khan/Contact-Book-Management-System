import csv
file_name = "contacts.csv"

print("CBMS -> ADD CONTACT FORM")

name = input("Enter Your Name: ")
email = input("Enter Your Email: ")
phone_no = input("Enter Your Phone Number: ")
address = input("Enter Your Address: ")

with open(file_name, "a", newline='') as file:
    fields = ["Name", "Email", "Phone Number", "Address"]

    writer = csv.DictWriter(file, fieldnames=fields)

    if file.tell() == 0:
        writer.writeheader()

    writer.writerow({"Name": name, "Email": email, "Phone Number": phone_no, "Address": address})

print("Contact saved successfully!")
