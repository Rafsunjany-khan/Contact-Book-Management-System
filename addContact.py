import csv

file_name = "contacts.csv"

def add_contacts():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")

    while True:
        try:
            phone_no = int(input("Enter Your Phone Number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the phone number.")

    address = input("Enter Your Address: ")

    # Check if the phone number already exists
    is_duplicate = False

    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["Phone Number"]) == phone_no:
                    is_duplicate = True
                    break

    except FileNotFoundError:
        pass

    if is_duplicate:
        print("This phone number is already saved. Please use another one.")
    else:
        with open(file_name, "a", newline='') as file:
            fields = ["Name", "Email", "Phone Number", "Address"]
            writer = csv.DictWriter(file, fieldnames=fields)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({"Name": name, "Email": email, "Phone Number": phone_no, "Address": address})

        print("Contact saved successfully!")
