a = input("Enter a character: ")

if a.isalpha():
    print(a, "is an alphabet.")
elif a.isdigit():
    print(a, "is a digit.")
else:
    print(a, "is a special character.")
