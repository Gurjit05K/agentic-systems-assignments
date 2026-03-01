# Take inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    
    # Check for negative age
    if age < 0:
        print("Age cannot be negative")
    else:
        # Print full name using concatenation
        full_name = first_name + " " + last_name
        print("Full Name:", full_name)
        
        # Print age next year
        print("You will be", age + 1, "next year")
        
except ValueError:
    print("Invalid age input")