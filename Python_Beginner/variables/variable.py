gross_salary = 50000
print(gross_salary)

##################
##################
income_tax = 5000
retirement_contribution = 1800
professional_tax = 300
net_salary = gross_salary - (income_tax + retirement_contribution + professional_tax)
print(net_salary)  # 42900

##################
##################
student1_score1 = 89
student2_score2 = 75
total_score = student1_score1 + student2_score2
print(total_score)  # 164

average_score = (student1_score1 + student2_score2) / 2

print(average_score)

##################
##################
first_name = "Alice"
last_name = "Bond"
full_name = first_name + " " + last_name
print(full_name)

##################
##################
my_int, my_float, my_bool, my_string = 12, 3.2, False, "Hello, World"
print(type(my_int), type(my_float), type(my_bool), type(my_string))

result = my_int + my_float
print("The final result is: ", result)

# result = my_int + my_string
# print("The final result is: ", result)  ## TypeError: unsupported operand type(s) for +: 'int' and 'str'

num = 10
num += 100
print(num)

num *= 10
print(num)

num //= 11
print(num) # we get a float, so we use '//' instead of '/'

num /= 4
print(num) # we get a float

num += 1
num %= 3
print(num)

num **= 4
print(num) # 16.0

print(net_salary)
del net_salary
print(net_salary) ## name 'net_salary' is not defined