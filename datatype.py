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
