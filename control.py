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


#Input a character and check if it is an alphabet, digit, or special character.
a = input("Enter a character: ")

if a.isalpha():
    print(a, "alphabet.")
elif a.isdigit():
    print(a, "digit.")
else:
    print(a, "character.")

#Input three numbers and print the largest among them. 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "largest")
elif b >= a and b >= c:
    print(b, "largest")
else:
    print(c, "largest")

#Input a number and check if it is divisible by 5 and 11 or not. 
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible  5 and 11.")
else:
    print(num, "is not divisible  5 and 11.")



#Input a number and check if it is a two-digit number or not.
num = 77

if num >=10 and age <=99:
    print(num, "is a two-digit number.")
else:
    print(num, "is not a two-digit number.")


a = int(input("Enter marks: "))

if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
else:
    print("Fail")

a = 85
b = 88
c = 85
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("valid")
else:
    print("not valid")

a = 88
b = 88
c = 66
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

a = " p"

if 'A' <= a <= 'Z':
    print("Uppercase")
elif 'a' <= a <= 'z':
    print("Lowercase")
else:
    print("Not alphabet")
