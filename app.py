# Function to perform addition
def addition(a, b):
    return a+b

# Function to perform subtraction
def subtraction(a, b):
    pass

# Function to perform multiplication
def multiplication(a, b):
    pass

# Function to perform division
def division(a, b):
    pass

# Main function
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", addition(num1, num2))
    print("Subtraction:", subtraction(num1, num2))
    print("Multiplication:", multiplication(num1, num2))
    print("Division:", division(num1, num2))

# Calling the main function
if __name__ == "__main__":
    main()
