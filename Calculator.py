
# Simple Calculator

def calculator():
    # Prompting the user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Displaying the available operations
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Taking the operation choice
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Performing the calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

# Running the calculator
calculator()
