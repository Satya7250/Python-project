def findVowel():
    userInput = input("Enter your string: ")
    count = 0
    vowelCount = 0
    specialCharCount = 0
    consoCount = 0
    spaces = 0

    for i in range(0, len(userInput)):
        count += 1  

        if userInput[i] in "aeiouAEIOU":
            vowelCount += 1
        
        elif userInput[i] in "!@#$%^&*()-=+[]{}<>.,/;:'\"\\|~":
            specialCharCount += 1
        
        elif userInput[i] == " ":
            spaces += 1

        elif userInput[i].isalpha():
            consoCount += 1

    print("Total Vowel: ", vowelCount)
    print("Total Consonant: ", consoCount)
    print("Spaces: ", spaces)
    print("Total no. of Special Characters: ", specialCharCount)
    print("Total number of characters: ", count)

print("Press 1 for Enter value")
print("Press 0 for exit")

i=1
while(i):
    choice = input("Enter your choice: ")
    if(choice =="0"):
        print("Program is exiting...!")
        i=0
    elif(choice == "1"):
        findVowel()
    else:
        print("Enter choice Again: ")