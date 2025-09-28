num = 123            # integer
str_num = str(num)   # convert to string
print(str_num)       # Output: '123'
print(type(str_num)) # <class 'str'>



text = "hello"           # string
char_list = list(text)   # convert to list of characters
print(char_list)         # Output: ['h', 'e', 'l', 'l', 'o']
print(type(char_list))   # <class 'list'>



my_list = [1, 2, 3, 4]   # list
my_tuple = tuple(my_list) 
print(my_tuple)          # Output: (1, 2, 3, 4)
print(type(my_tuple))    # <class 'tuple'>




my_tuple = (1, 2, 3, 2)  # tuple (can have duplicates)
my_set = set(my_tuple)   
print(my_set)            # Output: {1, 2, 3}  (duplicates removed)
print(type(my_set))      # <class 'set'>


# Program to demonstrate difference between mutable (list) and immutable (tuple)

# Mutable data type: List
my_list = [10, 20, 30]
print("Original List:", my_list)

# We can modify a list (e.g., change, add, or remove elements)
my_list[1] = 200
my_list.append(40)
print("Modified List:", my_list)  # List is changed successfully

# Immutable data type: Tuple
my_tuple = (10, 20, 30)
print("\nOriginal Tuple:", my_tuple)

# Trying to modify a tuple (this will cause an error)
try:
    my_tuple[1] = 200   # ❌ Tuples do not support item assignment
except TypeError as e:
    print("Error when trying to modify tuple:", e)

# Tuple remains unchanged
print("Tuple after modification attempt:", my_tuple)




# Create a dictionary with roll numbers as keys
students = {
    101: {"name": "Alice", "marks": 85},
    102: {"name": "Bob", "marks": 76},
    103: {"name": "Charlie", "marks": 92},
    104: {"name": "David", "marks": 67},
    105: {"name": "Eva", "marks": 88}
}

print("Students scoring more than 80:\n")

# Iterate through dictionary
for roll, details in students.items():
    if details["marks"] > 80:
        print(f"Roll No: {roll}, Name: {details['name']}, Marks: {details['marks']}")
