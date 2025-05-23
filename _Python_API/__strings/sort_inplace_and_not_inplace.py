# in place

strs = ["banana", "apple", "cherry"]
strs.sort()
print(strs)  # Output: ['apple', 'banana', 'cherry']

#####################################################

# non in-place
strs = ["banana", "apple", "cherry"]
sorted_strs = sorted(strs)
print(sorted_strs)  # Output: ['apple', 'banana', 'cherry']
print(strs)         # Output: ['banana', 'apple', 'cherry'] (original list is unchanged)
