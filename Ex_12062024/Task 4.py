#Fibonacci series

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
n = int(input("Enter a number: "))
print(fibonacci_recursive(n))