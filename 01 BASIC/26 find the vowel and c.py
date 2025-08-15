# Enter the singel character to find the vowel or consonant or special character
s = input("Enter the single character: ")

if (s == "a" or s == "e" or s == "i" or s == "o" or s == "u" or
    s == "A" or s == "E" or s == "I" or s == "O" or s == "U"):
    print("Vowel")
elif (s == "!" or s == "@" or s == "#" or s == "$" or s == "%" or
      s == "^" or s == "&" or s == "*" or s == "(" or s == ")" or
      s == "-" or s == "=" or s == "+" or s == "[" or s == "]" or
      s == "{" or s == "}" or s == "<" or s == ">" or s == "," or
      s == "." or s == "/" or s == ";" or s == ":" or s == "'" or
      s == "\"" or s == "\\" or s == "|" or s == "~"):
    print("Special Character")
else:
    print("Consonant")

