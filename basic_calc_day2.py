print("Welcome to the Basic Calculator")

# Define operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def mod(x, y):
    if y == 0:
        return "Error! Modulo by zero is not allowed."
    return x % y

# Main calculator loop
while True:
    print("\nEnter two numbers and choose an operation:")
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    print("Available operations: +, -, *, /, %")
    operation = input("Enter an operation to perform: ")

    # Perform the selected operation
    if operation == "+":
        result = add(x, y)
    elif operation == "-":
        result = subtract(x, y)
    elif operation == "*":
        result = multiply(x, y)
    elif operation == "/":
        result = divide(x, y)
    elif operation == "%":
        result = mod(x, y)
    else:
        print("Invalid operation! Please choose from +, -, *, /, %.")
        continue

    print(f"Result: {result}")

    # Ask the user if they want to continue
    done_operation_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    if done_operation_choice == "no":
        print("Goodbye! Thanks for using the calculator.")
        break
