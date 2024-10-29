cache = {}
cache[(1, 2, 3)] = "value1"
cache[(1, 2, 3)] = "value2"  # Overwrites the previous value
print(cache[(1, 2, 3)])  # Output: "value2"