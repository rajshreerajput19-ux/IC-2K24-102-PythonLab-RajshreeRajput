# Part A - Question 2: Employee Database
# Store employee records using dictionaries.
# Options: Add, Update Salary, Delete, Search, Reports, Exit.

employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}


def add_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ")
    dept = input("Enter department: ")

    try:
        salary = float(input("Enter salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary.")
        return

    employees[emp_id] = {
        "name": name,
        "dept": dept,
        "salary": salary
    }

    print("Employee added successfully.")


def update_salary():
    emp_id = input("Enter employee ID: ")

    if emp_id not in employees:
        print("Employee not found.")
        return

    try:
        salary = float(input("Enter new salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary.")
        return

    employees[emp_id]["salary"] = salary
    print("Salary updated successfully.")


def delete_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def search_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID:", emp_id)
        print("Details:", employees[emp_id])
    else:
        print("Employee not found.")


def show_reports():
    if not employees:
        print("No employee records available.")
        return

    payroll = {}
    headcount = {}
    highest_paid = {}

    # Department payroll and headcount in one pass
    for emp_id, data in employees.items():
        dept = data["dept"]
        salary = data["salary"]

        payroll[dept] = payroll.get(dept, 0) + salary
        headcount[dept] = headcount.get(dept, 0) + 1

        if dept not in highest_paid:
            highest_paid[dept] = data
        elif salary > highest_paid[dept]["salary"]:
            highest_paid[dept] = data

    print("\n--- Department Payroll and Headcount ---")

    for dept in payroll:
        print(dept, "Payroll:", payroll[dept])
        print(dept, "Headcount:", headcount[dept])

    print("\n--- Highest Paid Employee in Each Department ---")

    for dept, data in highest_paid.items():
        print(dept, ":", data["name"], "-", data["salary"])

    print("\n--- All Employees Sorted by Salary ---")

    sorted_employees = sorted(
        employees.items(),
        key=lambda item: item[1]["salary"],
        reverse=True
    )

    for emp_id, data in sorted_employees:
        print(emp_id, data["name"], data["salary"])

    print("\n--- 10% Raise for Employees Below 50000 ---")

    raised_salary = {
        emp_id: data["salary"] * 1.10
        for emp_id, data in employees.items()
        if data["salary"] < 50000
    }

    print(raised_salary)
    print("Original salaries are unchanged.")

    print("\n--- Department with Highest Average Salary ---")

    average_salary = {}

    for dept in payroll:
        average_salary[dept] = payroll[dept] / headcount[dept]

    best_dept = max(average_salary, key=average_salary.get)

    print("Department:", best_dept)
    print("Average Salary:", round(average_salary[best_dept], 2))


while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee by ID")
    print("5. Show Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        show_reports()
    elif choice == "6":
        print("Exiting Employee Database...")
        break
    else:
        print("Invalid choice. Try again.")

input("Press Enter to close the program...")