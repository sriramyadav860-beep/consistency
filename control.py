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



a = input("Enter a character: ")

if a.isalpha():
    print(a, "is an alphabet.")
elif a.isdigit():
    print(a, "is a digit.")
else:
    print(a, "is a special character.")


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "largest")
elif b >= a and b >= c:
    print(b, "largest")
else:
    print(c, "largest")


num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible  5 and 11.")
else:
    print(num, "is not divisible  5 and 11.")


num = 77

if num >=10 and age <=99:
    print(num, "is a two-digit number.")
else:
    print(num, "is not a two-digit number.")


