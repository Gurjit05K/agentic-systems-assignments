try:
    # Take two numbers as input
    num1_input = input("Enter first number: ")
    num2_input = input("Enter second number: ")
    
    # Convert to integers
    num1 = int(num1_input)
    num2 = int(num2_input)
    
    # Print sum
    print("Sum:", num1 + num2)
    
    # Check for division by zero
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        # Print division result
        print("Division result:", num1 / num2)
        
except ValueError:
    print("Invalid input")