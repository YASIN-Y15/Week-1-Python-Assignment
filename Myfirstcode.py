# SIMPLE CALCULATOR PROGRAM
# Basic Calculator with Specific Numbers

def main():
    print("=== CALCULATOR PROGRAM ===")
    print("This program demonstrates arithmetic operations")
    print("using the numbers from your assignment: 10 and 5\n")
    
    # Using the exact numbers 
    num1 = 10
    num2 = 5
    
    # Display the numbers being used
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print()
    
    # Perform all operations as per assignment requirements
    print("Performing all operations from the assignment:")
    print("---------------------------------------------")
    
    # Addition
    addition_result = num1 + num2
    print(f"ADDITION: {num1} + {num2} = {addition_result}")
    
    # Subtraction
    subtraction_result = num1 - num2
    print(f"SUBTRACTION: {num1} - {num2} = {subtraction_result}")
    
    # Multiplication
    multiplication_result = num1 * num2
    print(f"MULTIPLICATION: {num1} * {num2} = {multiplication_result}")
    
    # Division
    if num2 != 0:
        division_result = num1 / num2
        print(f"DIVISION: {num1} / {num2} = {division_result}")
    else:
        print("DIVISION: Cannot divide by zero!")
    
    print("\n=== PROGRAM COMPLETED ===")
    print("Thank you for using the calculator!")

# Run the program
if __name__ == "__main__":
    main()