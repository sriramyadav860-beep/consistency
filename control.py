num = 9

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

num = 8

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

a = 8
b = 5

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")

a = 16
b = 16

if a == b:
    print("Both numbers are equal")
else:
    print("The numbers are not equal")

age = 20
if age >=18 and age <=20:
    print("eligible")
else:
    print("not eligible")



ch = input("4")

if ch.isalpha():
    print(ch, "is an alphabet.")
elif ch.isdigit():
    print(ch, "is a digit.")
else:
    print(ch, "is a special character.")
