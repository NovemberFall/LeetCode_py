from collections import defaultdict

'''
- The defaultdict is a subclass of the built-in dict class in Python's collections module. 
- It overrides one method and adds one writable instance variable.
 
- The primary purpose of defaultdict is to provide a default value for the dictionary being accessed 
    when a key is not present. 
    
- This avoids the need for explicit checks to see if a key exists in the dictionary 
    before accessing or modifying its value.
'''


# Default factory function to provide a default integer (0)
def default_int():
    return 0

# Create a defaultdict with default value 0 for missing keys
d = defaultdict(default_int)

# Add some key-value pairs
d['a'] = 1
d['b'] = 2

print(d['a'])  # Output: 1
print(d['b'])  # Output: 2
print(d['c'])  # Output: 0, since 'c' is not present, it gets default value 0





'''
The above example can be simplified using the built-in `int` as the default factory, which returns 0:
'''

# Create a defaultdict with default value 0 for missing keys
dint = defaultdict(int)

# Add some key-value pairs
dint['a'] = 1
dint['b'] = 2

print(dint['a'])  # Output: 1
print(dint['b'])  # Output: 2
print(dint['c'])  # Output: 0, since 'c' is not present, it gets default value 0

