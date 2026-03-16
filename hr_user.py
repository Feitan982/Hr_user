import datetime

# In-memory "database"
users = [
    {"hr_id": 1, "name": "Admin", "username": "admin", "password": "admin123", "role": "Admin", "contact_number": "0900000000"}
]

departments = []
employees = []
attendance_records = []

# ---------------- LOGIN ----------------

def login():
    print("\nHR MANAGEMENT SYSTEM LOGIN")
    username = input("Username: ")
    password = input("Password: ")
    
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login Successful\n")
            return True
    print("Invalid Login\n")
    return False

# ---------------- DEPARTMENT ----------------

def add_department():
    department_id = len(departments) + 1
    name = input("Department Name: ")
    location = input("Location: ")
    departments.append({"department_id": department_id, "department_name": name, "location": location})
    print("Department Added\n")

def view_departments():
    print("\nDEPARTMENT LIST\n")
    print("{:<5} {:<20} {:<20}".format("ID", "DEPARTMENT", "LOCATION"))
    print("-" * 45)
    for dept in departments:
        print("{:<5} {:<20} {:<20}".format(dept["department_id"], dept["department_name"], dept["location"]))

# ---------------- EMPLOYEE ----------------

def add_employee():
    employee_id = len(employees) + 1
    name = input("Name: ")
    address = input("Address: ")
    contact = input("Contact Number: ")
    position = input("Position: ")
    dept_id = int(input("Department ID: "))
    date_hired = input("Date Hired (YYYY-MM-DD): ")
    status = input("Status: ")
    
    # Check department exists
    if not any(d["department_id"] == dept_id for d in departments):
        print("Department ID not found.\n")
        return
    
    employees.append({
        "employee_id": employee_id,
        "name": name,
        "address": address,
        "contact_number": contact,
        "position": position,
        "department_id": dept_id,
        "date_hired": date_hired,
        "status": status
    })
    print("Employee Added\n")

def view_employees():
    print("\nEMPLOYEE LIST\n")
    print("{:<5} {:<20} {:<15} {:<15} {:<10}".format("ID", "NAME", "POSITION", "STATUS", "DEPT"))
    print("-" * 70)
    for emp in employees:
        print("{:<5} {:<20} {:<15} {:<15} {:<10}".format(
            emp["employee_id"],
            emp["name"],
            emp["position"],
            emp["status"],
            emp["department_id"]
        ))

# ---------------- ATTENDANCE ----------------

def record_attendance():
    emp_id = int(input("Employee ID: "))
    time_in = input("Time In: ")
    time_out = input("Time Out: ")
    status = input("Status: ")
    date = str(datetime.date.today())
    
    # Check employee exists
    if not any(e["employee_id"] == emp_id for e in employees):
        print("Employee ID not found.\n")
        return
    
    attendance_id = len(attendance_records) + 1
    attendance_records.append({
        "attendance_id": attendance_id,
        "employee_id": emp_id,
        "date": date,
        "time_in": time_in,
        "time_out": time_out,
        "status": status
    })
    print("Attendance Recorded\n")

def view_attendance():
    print("\nATTENDANCE RECORDS\n")
    print("{:<5} {:<10} {:<12} {:<10} {:<10} {:<10}".format(
        "ID", "EMP_ID", "DATE", "TIME_IN", "TIME_OUT", "STATUS"))
    print("-" * 65)
    for record in attendance_records:
        print("{:<5} {:<10} {:<12} {:<10} {:<10} {:<10}".format(
            record["attendance_id"],
            record["employee_id"],
            record["date"],
            record["time_in"],
            record["time_out"],
            record["status"]
        ))

# ---------------- MENU ----------------

def menu():
    while True:
        print("""
HR MANAGEMENT SYSTEM

1 Add Department
2 View Departments
3 Add Employee
4 View Employees
5 Record Attendance
6 View Attendance
7 Exit
""")
        choice = input("Choose option: ")
        if choice == "1":
            add_department()
        elif choice == "2":
            view_departments()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            view_employees()
        elif choice == "5":
            record_attendance()
        elif choice == "6":
            view_attendance()
        elif choice == "7":
            print("System Closed")
            break
        else:
            print("Invalid Option")

# ---------------- MAIN ----------------

if login():
    menu()