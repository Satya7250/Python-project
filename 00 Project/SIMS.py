students = {
    '01': {'Name': 'satya', 'Branch': 'cse', 'Admission Year': 2023, 'Contact': ('444', 'satya@'), 'AcademicHistory': (2, 7.0, 2023)}, 
    '02': {'Name': 'Ritika', 'Branch': 'fpp', 'Admission Year': 2023, 'Contact': ('44', 'ritika@'), 'AcademicHistory': (3, 6.0, 2026)}
}

def addNewStudent():
    roll = input("Enter your rollNum: ").strip()
    if(roll in students):
        print("Student with this roll already exists...!")
        return 
    name = input("Enter your Name: ")
    branch = input("Enter your Branch: ").strip()

    admissionYear = input("Enter your Admission Year: ")
    if not admissionYear.isdigit() or int(admissionYear) <=0:
        print("Invalid Admission Year")
        return
    admissionYear = int(admissionYear)
    phone = input("Enter phone number: ").strip()
    email = input("Enter your email: ").strip()

    lastSem = input("Enter last completed sem: ")
    if not lastSem.isdigit():
        print("Invalid lastSem")
        return
    lastSem = int(lastSem)

    cgpa = input("Enter your CGPA: ").strip()
    cgpa = float(cgpa)

    semYear = input("Enter your Semester Year: ").strip()
    if not semYear.isdigit() or int(semYear) <=0:
        print("Invalid Semester Year")
        return
    semYear = int(semYear)

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Admission Year": admissionYear,
        "Contact": (phone,email),
        "AcademicHistory": (lastSem,cgpa,semYear)
    }
    print("Student added Successfully!")

def displayAllStudents():

    print("+----------+-----------------+------------+--------+")
    print("| Roll     | Name            | Branch     | CGPA   |")
    print("+----------+-----------------+------------+--------+")

    for roll, details in students.items():
       name = details['Name']
       branch = details['Branch']
       cgpa = details['AcademicHistory'][1]
       print(f"| {roll:<8} | {name:<15} | {branch:<10} | {cgpa:<6} |")

    print("+----------+-----------------+------------+--------+")

def fetchDetails():
    newRoll = input("Enter Roll for Details: ")
    if newRoll in students:
        print("Student Details:", students[newRoll])
    else:
        print("No student found with this roll number.")


def searchByBranch():
    branch = input("Enter the branch: ").strip().lower()
    l3 = 0
    for roll, info in students.items():
        if info['Branch'].lower() == branch:
            print(f"Roll:{roll}, Name:{info['Name']}")
            l3 = 1
    if not l3:
        print("No Data found of this Branch")


def updateDetails():
    nRoll = input("Enter Roll of Student: ")
    if nRoll in students:
        l2 = 1
        print("Press 1 for Name")
        print("Press 2 for Branch")
        print("Press 3 for Admission Year")
        print("Press 4 for Contact Info")
        print("Press 5 for AcademicHistory")
        print("Press 0 for Exit from updateDetails")

        while(l2):
            cho2 = input("Enter your Choice: ")
            if(cho2 == '0'):
                print("UpdateDetails is Closed..!")
                l2 = 0
            elif(cho2 == '1'):
                newName = input("Enter new Name: ")
                students[nRoll]['Name'] = newName
                print("Name updated.")
            elif(cho2 == '2'):
                newBranch = input("Enter new Branch: ")
                students[nRoll]['Branch'] = newBranch
                print("Branch updated.")
            elif(cho2 == '3'):
                newYear = input("Enter new Admission Year: ")
                if not newYear.isdigit() or int(newYear) <= 0:
                    print("Invalid Admission Year.")
                else:
                    students[nRoll]['Admission Year'] = int(newYear)
                    print("Admission Year updated.")
            elif(cho2 == '4'):
                newPhone = input("Enter new Phone: ").strip()
                newEmail = input("Enter new Email: ").strip()
                students[nRoll]['Contact'] = (newPhone, newEmail)
                print("Contact Info updated.")
            elif(cho2 == '5'):
                lastSem = input("Enter last completed sem: ")
                if not lastSem.isdigit():
                   print("Invalid semester.")
                   continue
                lastSem = int(lastSem)
                cgpa = input("Enter CGPA: ")
                cgpa = float(cgpa)
                semYear = input("Enter Semester Year: ")
                if not semYear.isdigit() or int(semYear) <= 0:
                   print("Invalid Semester Year.")
                   continue

                semYear = int(semYear)
                students[nRoll]['AcademicHistory'] = (lastSem, cgpa, semYear)
                print("Academic History updated.")
            else:
               print("Invalid choice. Try again.")


def compareAcademic():
    rollOne = input("Enter rollOne").strip()
    rollTwo = input("Enter rollTwo").strip()
    if rollOne and rollTwo in students:



l=1
print("Press 1 for Add Student Details: ")
print("Press 2 for Display allDetails: ")
print("Press 3 for Fetch Details")
print("Press 4 for Update Details")
print("Press 5 for Search By Branch")
print("Press 6 for compare by CGPA")
print("Press 0 for Exit...!")

while(l):
    choice = input("Enter your Choice: ")
    if(choice == '0'):
        print("Program is Exiting...!")
        l=0
    elif(choice == '1'):
        addNewStudent()
    elif(choice == '2'):
        if students == {}:
            print("No Data Found..!")
        else:
            displayAllStudents()
    elif(choice == '3'):
        fetchDetails()
    elif(choice == '4'):
        updateDetails()
    elif(choice == '5'):
        searchByBranch()
    elif(choice == '6'):
        compareAcademic()
    