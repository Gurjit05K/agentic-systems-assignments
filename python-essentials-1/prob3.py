# Take inputs
name = input("Enter your name: ")

try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    
    # Check for negative age
    if age < 0:
        print("Age cannot be negative")
    else:
        # Print greeting
        print("Hello", name)
        
        # Determine age category
        if age < 13:
            print("You are a Child")
        elif 13 <= age <= 17:
            print("You are a Teenager")
        elif 18 <= age <= 59:
            print("You are an Adult")
        else:  # 60 and above
            print("You are a Senior Citizen")
        
        # Check voting eligibility
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")
            
except ValueError:
    print("Invalid age input")