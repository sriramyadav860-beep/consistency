# Add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result = a + b
print("The sum is:", sum_result)


a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)          # normal division
print("Floor Division:", a // b)   # quotient only
print("Modulus:", a % b)           # remainder
print("Power:", a ** b)            # a^b


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
