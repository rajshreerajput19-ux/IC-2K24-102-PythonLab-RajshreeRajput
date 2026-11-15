# Part A - Question 3: Library Record System
# Store books using ISBN as dictionary key.
# Options: Add Book, Issue, Return, Search, Reports, Exit.

books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}


def add_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        try:
            copies = int(input("Enter additional copies: "))
            if copies <= 0:
                print("Copies must be greater than zero.")
                return
            books[isbn]["copies"] += copies
            print("Copies added successfully.")
        except ValueError:
            print("Enter a valid number.")
        return

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    try:
        copies = int(input("Enter number of copies: "))
        if copies <= 0:
            print("Copies must be greater than zero.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    books[isbn] = {
        "title": title,
        "author": author,
        "copies": copies,
        "issued_to": []
    }

    print("Book added successfully.")


def issue_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found.")
        return

    book = books[isbn]

    if member in book["issued_to"]:
        print("This member already has this book.")
        return

    total_issued = 0

    for data in books.values():
        total_issued += data["issued_to"].count(member)

    if total_issued >= 2:
        print("A member cannot issue more than 2 books.")
        return

    if book["copies"] <= 0:
        print("Book is not available.")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)

    print("Book issued successfully.")


def return_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found.")
        return

    book = books[isbn]

    if member not in book["issued_to"]:
        print("This member has not issued this book.")
        return

    book["issued_to"].remove(member)
    book["copies"] += 1

    print("Book returned successfully.")


def search_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        print("ISBN:", isbn)
        print("Book Details:", books[isbn])
    else:
        print("Book not found.")


def show_reports():
    print("\n--- Books by Author ---")

    author_name = input("Enter author name: ").lower()

    result = {
        isbn: data["title"]
        for isbn, data in books.items()
        if author_name in data["author"].lower()
    }

    print(result if result else "No books found.")

    print("\n--- Members Holding More Than One Book ---")

    member_books = {}

    for isbn, data in books.items():
        for member in data["issued_to"]:
            member_books.setdefault(member, []).append(data["title"])

    found = False

    for member, titles in member_books.items():
        if len(titles) > 1:
            print(member, ":", titles)
            found = True

    if not found:
        print("No member is holding more than one book.")

    print("\n--- Unavailable Books ---")

    unavailable = {
        isbn: data["title"]
        for isbn, data in books.items()
        if data["copies"] == 0
    }

    print(unavailable if unavailable else "No unavailable books.")

    print("\n--- Never Issued Books ---")

    never_issued = {
        isbn: data["title"]
        for isbn, data in books.items()
        if len(data["issued_to"]) == 0
    }

    print(never_issued if never_issued else "All books have been issued at least once.")


while True:
    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Show Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        show_reports()
    elif choice == "6":
        print("Exiting Library System...")
        break
    else:
        print("Invalid choice. Try again.")

input("Press Enter to close the program...")