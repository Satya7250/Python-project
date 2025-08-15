mark = float(input("Enter the student marks: "))

if 0 <= mark <= 100:
    if mark >= 90:
        print("Grade is A+")
    elif mark >= 80:
        print("Grade is A")
    elif mark >= 70:
        print("Grade is B+")
    elif mark >= 60:
        print("Grade is B")
    else:
        print("Fail Grade: E")
else:
    print("Invalid Marks, please Enter Again")
