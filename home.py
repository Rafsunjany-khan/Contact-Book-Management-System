print("Welcome To Contact Book Management System")
print("1. For Add User Contact")
print("2. For View Contact")
print("3. For Search Contact")
print("4. For Remove Contact")
print("5. For Exit")

choice = input("Enter Your Choice: ")

if choice == "1":
    import addContact
elif choice == "2":
    import view
elif choice == "3":
    import search
elif choice == "4":
    import remove
elif choice == "5":
    print("Good Bye")
else:
    print("Invalid Input!")