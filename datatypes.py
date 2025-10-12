"hello" + "world"

s = "abc"
result = s * 3
print(result)  # prints: abcabcabc


s = "python"
first_char = s[0]
last_char = s[-1]
print(first_char, last_char)  # prints: p n

s = "programming"
sub = s[:6]   # takes from index 0 up to (but not including) index 6
print(sub)    # prints: progra




s = "hello"
reversed_s = s[::-1]
print(reversed_s)  


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


x = 10              # int
y = 10.5            # float
z = "Hello"         # string
b = True            # boolean
l = [1, 2, 3]       # list
t = (1, 2, 3)       # tuple
s = {1, 2, 3}       # set
d = {"name": "Ram", "age": 21}  # dictionary

print(type(x))
print(type(z))
