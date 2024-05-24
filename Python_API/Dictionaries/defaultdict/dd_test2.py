from collections import defaultdict

'''
Example 1: Counting Occurrences
'''


# Create a defaultdict with default value 0 for counting
word_count = defaultdict(int)

# List of words
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Count occurrences of each word
for word in words:
    word_count[word] += 1

print(word_count)
# Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})









'''
Example 2: Grouping Items
'''

# Create a defaultdict with default value as an empty list
students_courses = defaultdict(list)

# List of students and their courses
students = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'Science'), ('Bob', 'Math')]

# Group students by courses
for student, course in students:
    students_courses[student].append(course)

print(students_courses)
# Output: defaultdict(<class 'list'>, {'Alice': ['Math', 'Science'], 'Bob': ['Science', 'Math']})