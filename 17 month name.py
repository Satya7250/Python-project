#print corresponding month name
months = ["January","February","March","April","May","June",
    "July","August","September","October","November","December"]
num = int(input("Enter the number: "))
if (1 <= num <= 12):
    print(months[num - 1])
else:
    print("Invalid")
