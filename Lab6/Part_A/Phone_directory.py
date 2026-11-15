# Part A - Question 5: Phone Directory
# Store contacts using name as dictionary key.
# Options: Add Contact, Add Number, Update Details,
# Delete, Search, Reports, Exit.

contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@gmail.com",
        "city": "Indore"
    },
    "Manoj": {
        "phones": ["9876543211", "9876543212"],
        "email": "manoj@gmail.com",
        "city": "Bhopal"
    },
    "Zara": {
        "phones": ["9876543213"],
        "email": "zara@gmail.com",
        "city": "Indore"
    }
}


def valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()


def phone_exists(phone):
    for name, data in contacts.items():
        if phone in data["phones"]:
            return True
    return False


def add_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter 10-digit phone number: ")

    if not valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if phone_exists(phone):
        print("This phone number already belongs to another contact.")
        return

    email = input("Enter email: ")
    city = input("Enter city: ")

    contacts[name] = {
        "phones": [phone],
        "email": email,
        "city": city
    }

    print("Contact added successfully.")


def add_number():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ")

    if not valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if phone_exists(phone):
        print("This phone number is already saved.")
        return

    contacts[name]["phones"].append(phone)
    print("Phone number added successfully.")


def update_contact():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found.")
        return

    email = input("Enter new email: ")
    city = input("Enter new city: ")

    contacts[name]["email"] = email
    contacts[name]["city"] = city

    print("Contact details updated successfully.")


def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact():
    search_name = input("Enter full or partial name: ").lower()

    found = False

    for name, data in contacts.items():
        if search_name in name.lower():
            print(name, ":", data)
            found = True

    if not found:
        print("Contact not found.")


def show_reports():
    print("\n--- Reverse Phone Lookup ---")

    phone_directory = {
        phone: name
        for name, data in contacts.items()
        for phone in data["phones"]
    }

    print(phone_directory)

    print("\n--- Contacts Grouped by City ---")

    city_contacts = {}

    for name, data in contacts.items():
        city = data["city"]
        city_contacts.setdefault(city, []).append(name)

    print(city_contacts)

    print("\n--- Contacts with Multiple Numbers ---")

    found = False

    for name, data in contacts.items():
        if len(data["phones"]) > 1:
            print(name, ":", data["phones"])
            found = True

    if not found:
        print("No contacts have multiple numbers.")

    print("\n--- Complete Directory in Alphabetical Order ---")

    for name in sorted(contacts):
        print(name, ":", contacts[name])


while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email and City")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Show Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        add_number()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        show_reports()
    elif choice == "7":
        print("Exiting Phone Directory...")
        break
    else:
        print("Invalid choice. Try again.")

input("Press Enter to close the program...")