# Task 2: Using the Math Module

import math # Importing the required module

# 1. Asks the user for a number as input 
try:
    user_input = float(input("Enter a number: "))

    # 2. Uses the math module to calculate specific values
    square_root = math.sqrt(user_input) # Square root
    
    # Natural logarithm (base e). Note: number must be > 0
    if user_input > 0:
        logarithm = math.log(user_input) 
    else:
        logarithm = "Undefined (input must be greater than 0)"
        
    sine_value = math.sin(user_input) # Sine in radians

    # 3. Displays the calculated results 
    print(f"Square root: {square_root}") 
    print(f"Logarithm: {logarithm}") 
    print(f"Sine: {sine_value}")

except ValueError:
    print("Invalid input. Please enter a numerical value.")
