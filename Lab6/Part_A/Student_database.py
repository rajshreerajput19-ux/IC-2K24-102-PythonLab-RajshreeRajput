# Part A - Question 1: Student Database
# Store student details using nested dictionaries.
# Options: Add, Update, Delete, Show Record, Reports, Exit.

students = {
    "101": {
        "name": "Asha",
        "marks": {"Math": 88, "Physics": 76, "Chemistry": 92}
    },
    "102": {
        "name": "Ravi",
        "marks": {"Math": 35, "Physics": 58, "Chemistry": 64}
    },
    "103": {
        "name": "Meena",
        "marks": {"Math": 72, "Physics": 81, "Chemistry": 69}
    }
}


def get_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Duplicate roll number! Student already exists.")
        return

    name = input("Enter student name: ")
    marks = {}

    count = int(input("How many subjects? "))

    for i in range(count):
        subject = input("Enter subject name: ")
        marks[subject] = get_marks()

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")


def update_marks():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ")
    marks = get_marks()

    students[roll]["marks"][subject] = marks
    print("Marks updated successfully.")


def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_record():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Roll Number:", roll)
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.")


def show_reports():
    if not students:
        print("No student records available.")
        return

    averages = {}

    print("\n--- Average Marks ---")

    for roll, data in students.items():
        marks = data["marks"]

        if marks:
            average = sum(marks.values()) / len(marks)
            averages[roll] = average
            print(data["name"], ":", round(average, 2))
        else:
            averages[roll] = 0
            print(data["name"], ": No marks available")

    topper = max(averages, key=averages.get)
    print("\nTopper:", students[topper]["name"])

    print("\n--- Highest Scorer in Each Subject ---")

    subjects = {}

    for data in students.values():
        for subject in data["marks"]:
            subjects[subject] = True

    for subject in subjects:
        highest = None
        highest_marks = -1

        for roll, data in students.items():
            if subject in data["marks"]:
                if data["marks"][subject] > highest_marks:
                    highest_marks = data["marks"][subject]
                    highest = data["name"]

        print(subject, ":", highest, "-", highest_marks)

    print("\n--- Students Below 40 ---")

    found = False

    for data in students.values():
        for subject, marks in data["marks"].items():
            if marks < 40:
                print(data["name"], "-", subject, ":", marks)
                found = True

    if not found:
        print("No students below 40.")

    print("\n--- Grade-wise Grouping ---")

    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, average in averages.items():
        name = students[roll]["name"]

        if average >= 90:
            grades["A"].append(name)
        elif average >= 75:
            grades["B"].append(name)
        elif average >= 60:
            grades["C"].append(name)
        elif average >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print(grades)


while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. Update Subject Marks")
    print("3. Delete Student")
    print("4. Show Full Record")
    print("5. Show Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_record()
    elif choice == "5":
        show_reports()
    elif choice == "6":
        print("Exiting Student Database...")
        break
    else:
        print("Invalid choice. Try again.")

input("Press Enter to close the program...")