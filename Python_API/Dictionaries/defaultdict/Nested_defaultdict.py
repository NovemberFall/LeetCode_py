from collections import defaultdict

'''
Example 3: Nested defaultdict
'''



# Create a nested defaultdict
nested_dict = defaultdict(lambda: defaultdict(int))

# Add some data
nested_dict['Math']['Alice'] = 95
nested_dict['Science']['Bob'] = 88

print(nested_dict)
'''
Output: defaultdict(<function <lambda> at 0x7f8e4cfa3940>, 
    {
        'Math': defaultdict(<class 'int'>, {'Alice': 95}), 
        'Science': defaultdict(<class 'int'>, {'Bob': 88})
    })
'''

# Accessing a missing key in nested dictionary returns a defaultdict
print(nested_dict['Math']['Charlie'])  # Output: 0, because of the inner defaultdict(int)
