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


