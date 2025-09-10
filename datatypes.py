decimal_num = 5.5
integer_num = int(decimal_num)
print("decimal",decimal_num)
print("integer",integer_num)

a = 5.4
b = int(a)
print("deci",a)
print("int",b)

a = "sriram"
b = 7
c = 5.5
print("the type of 'a",type(a))
print("type 'b",type(b))
print("type 'c",type(c))


a = "100"
b = int(a)
result = b + 50
print(result)

# Assign an integer to the variable
x = 42
print("x as integer:", x)

# Reassign a string to the same variable
x = "Python"
print("x as string:", x)

# Reassign a float to the same variable
x = 3.14159
print("x as float:", x)



# Take input from the user
user_input = input(123)

# Print the input and its data type
print("You entered:", user_input)
print("Data type:", type(user_input))



# Input: two integers
a = 5
b = 10


# Swapping using tuple unpacking
a, b = b, a

# Output after swap
print("After swapping:")
print("a =", a)
print("b =", b)






# Take input from the user
text = input("sriram ")

# Initialize an empty string for the reversed version
reversed_text = ""

# Loop through the string in reverse order
for char in text:
    reversed_text = char + reversed_text  # Prepend each character

# Print the reversed string
print("Reversed string:", reversed_text)
