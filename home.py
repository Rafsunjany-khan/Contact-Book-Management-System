import addContact
import search
import view
import remove

print("Welcome To Contact Book Management System")
print("1. For Add User Contact")
print("2. For View Contact")
print("3. For Search Contact")
print("4. For Remove Contact")
print("5. For Exit")

while True:
    choice = input("Enter Your Choice: ")
    if choice == "1":
        print("CBMS -> VIEW ALL CONTACTS")
        view.view_contacts()

    elif choice == "2":
        print("CBMS -> ADD CONTACT FORM")
        addContact.add_contacts()

    elif choice == "3":
        print("CBMS -> SEARCH CONTACT")
        search_name = input("Enter Your Searching Name....: ")
        search.search_contact(search_name)

    elif choice == "4":
        print("CBMS -> REMOVE CONTACT")
        remove.remove_contacts()

    elif choice == "5":
        print("Good Bye, Thanks for Using CBMS")
        break
    else:
        print("Invalid Input!")