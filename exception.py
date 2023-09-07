print("Write a program that asks the user for a number and handles exceptions (e.g., ValueError) if the user enters something that's not a number.")

try:
    number = float(input("Enter any number: "))
    print(f"Your number is {number}.")
except ValueError:
    print("Invalid number.Please enter valid number. ")    