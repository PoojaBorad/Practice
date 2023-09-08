print("Build a simple calculator that can perform addition, subtraction, multiplication, and division based on user input.")

print("Choices:")
print("Enter '1' for addition")
print("Enter '2' for subtraction")
print("Enter '3' for multiplication")
print("Enter '4' for division")
print("Enter '0' to end the program")

user_input = int(input("Please enter your choice: "))

if user_input == 0:
    exit()

if user_input in [1, 2, 3, 4]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_input == 1:
        result = num1 + num2
    elif user_input == 2:
        result = num1 - num2
    elif user_input == 3:
        result = num1 * num2
    elif user_input == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
            exit()
        result = num1 / num2

    print("Result:", result)
else:
    print("Invalid input. Please try again.")
