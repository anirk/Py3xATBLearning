

#Explain the difference between = and == operator in python
# Using the assignment operator
#The = operator is used to assign a value to a variable.
x = 10
y = 20


# What does the ** operator do in Python, and how is it used?
# ** operator is an Airthematic operator, it performs exponentiation,raising the first operand value to the right operand value.

#For example,
a = 2
b = 3
c = a ** b
print(c)

#In Python, the ^ operator is the bitwise XOR (exclusive OR) operator.
# It performs a bitwise XOR operation on two integers.
# The result of this operation is a new integer where each bit is set to 1 if the corresponding bits of the operands are different,
# and set to 0 if they are the same.

# For example,
x = 7 # 0111 (8421)
y = 4 # 0100 (8421)
z = x ^ y # 0011
print(z)

# Using the equality operator
#The == operator is used to compare two values to check if they are equal
# Using the assignment operator
x = 10
y = 20

# Using the equality operator
print(x == y)  # Output: False
print(x == 10) # Output: True

# Reassigning y
y = 10
print(x == y)  # Output: True



#Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8


import math

number = int(input("Enter the number\n"))
print(number)
sqr = math.pow(number,2)
print(sqr)
cube=math.pow(number,3)
print(cube)