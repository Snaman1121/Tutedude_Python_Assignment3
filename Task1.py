# Task 1: Calculate Factorial Using a Function

# 1. Defines a function named factorial that takes a number as an argument
def factorial(n):
    # Calculations using a loop
    result = 1
    for i in range(1, n + 1):
        result *= i
    # 2. Returns the calculated factorial
    return result

# 3. 3. Calls the function with a sample number and prints the output

try:

    num = int(input("Enter a number:"))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        output = factorial(num)
        print(f"Factorial of {num} is: {output}")
except ValueError:
    print("Please enter a valid integer.")
