#Write a program to create, concatenate and print a string and accessing sub-string from a given string.

string1 = "Hello"
string2 = "World"

# Concatenating strings
concatenateString = string1 + " " + string2

# Printing the concatenated string
print("Concatenated String:", concatenateString)

# Accessing sub-strings
print("Substring (0 to 4):", concatenateString[0:5])  # "Hello"
print("Substring (6 to 10):", concatenateString[6:])  # "World"
