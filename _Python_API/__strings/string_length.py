my_string = "Hello, World!"
length = len(my_string)
print(length)  # Output: 13

##################################################

strings = ["apple", "banana", "kiwi", "date"]

# Filtering __strings that are longer than 4 characters
long_strings = [s for s in strings if len(s) > 4]

print(long_strings)  # Output: ['apple', 'banana']



##################################################

strings = ["Hello", "World", "Python"]

for s in strings:
    print(f"The length of '{s}' is {len(s)} characters.")
