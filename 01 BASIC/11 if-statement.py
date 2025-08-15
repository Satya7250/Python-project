#if condition is true then statements will be executed.
mark = float(input("Enter the student marks: "))
if((mark<=100) and (mark>=40)):
    if((mark>=90) and (mark <= 100)):
        print("Grade is A+")
    if((mark>=80) and (mark<90)):
        print("Grade is A")
    if((mark>=70) and (mark<80)):
        print("Grade is B+")
    if((mark>=60) and (mark<70)):
        print("Grade is B")
    if((mark>=50) and (mark<60)):
        print("Grade is C+")
    if((mark>=40) and (mark<50)):
        print("Grade is C")
if((mark<40) and (mark>=0)):
    print("Fail Grade: E")
if((mark>100) or (mark<0)):
    print("Invalid Marks please Enter Again")
