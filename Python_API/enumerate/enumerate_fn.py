def test_enumerate():
    nums = [2, 7, 11, 15]
    for i, num in enumerate(nums):
        print(f"Index: {i}, Value: {num}")


test_enumerate()

"""
The enumerate() function in Python is used to iterate over an iterable object, like a list or tuple, 
and return an enumerate object. 
This enumerate object produces a series of tuples where each tuple contains two elements:
    1. Index (counter): An integer value representing the current position (index) within the iterable. 
    This starts from 0.
    
    2. Element: The value from the original iterable at the corresponding index.
"""