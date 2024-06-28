# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1=int(input("enter the first number\n"))
num2=int(input("enter the second number\n"))
result= ("first number is greater than second" if num1>num2
         else "first number is lesser than second" if num1<num2
         else "first number is equal to second")
print(result)