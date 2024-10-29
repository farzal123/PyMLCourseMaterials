# Accessing dict Values
# Values in dict are accessed using their keys
# If a key isn't found, a KeyError will be raised unless the get() method is used that returns None

#Example
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
 
# Accessing values with keys
 
name = my_dict['name']
age = my_dict.get('age')
 
# Printing accessed values
print(f'Name = {name}')
print(f'Age = {age}')
 
 