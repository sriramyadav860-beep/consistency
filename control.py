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

#Input a date (day, month, year) and check if it is valid.
a = 21
b = 6
c = 2005

if a > 0 and a < 31 and b > 0 and b < 13 and c > 1600 and  c < 9999:
    print(a,b,c)
else:
    print("invaild")


#Input three numbers and check if they can form a Pythagorean triplet
a = 3
b = 4
c = 5
if a*a + b*b == c*c:
    print("true")
else:
    print("false")


#Input time (hours, minutes) and check if it is a valid time.

a = 5
b = 59

if a >= 1 and a <= 12 and b >= 0 and b <= 60:
    print(a,b , "valid")
else:
    print("in valid")



    
#Input a year and print the century it belongs to.

year = 9000

century = (year - 1) // 100 + 1

print(f"{century} century.")


# Input a day number (1–7) and print the day of the week

day = 5

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day ")




# Input a month number (1–12) and print the number of days in that month

month = int(input("Enter month number (1–12): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 2:
    print("28 or 29 days (February)")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")


# hex_check_strict.py
ch = input("Enter a single character: ").strip()

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch in "0123456789ABCDEF":
        print(f"'{ch}' is a hexadecimal digit (0-9, A-F).")
    else:
        print(f"'{ch}' is NOT a hexadecimal digit (0-9, A-F).")


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

#Electricity Bill Calculator
#Input units consumed:
#First 100 units → ₹5 per unit
#Next 100 units → ₹8 per unit
#Above 200 units → ₹10 per uni
units = 100
if units <= 100:
    print( 5*units)
elif units >= 100 and units <= 199:
    print(8*units)
elif units  >= 200:
    print(10*units)

#Discount Calculator
#Input the total shopping amount:
#If amount > 5000 → 20% discount If amount > 2000 → 10% discount Otherwise → no discountamount = 2000
amount = 5000

if amount >= 2000 and amount <5000:
    print("20% discount")
elif amount >= 5000:
    print("30% discount")
else:
    print(amount)



amount = 9000

if amount >= 2000 and amount <5000:
    print( amount - amount * 0.20 )
elif amount >= 5000:
    print(amount - amount * 0.30)
else:
    print(amount)


#tempernatur
temp = 5
if temp <= 0:
    print("frezz")
elif temp >= 1 and temp <=20:
    print("cool")
elif temp >= 21 and temp <=35:
    print("warm")
elif temp > 35:
    print("hot")


