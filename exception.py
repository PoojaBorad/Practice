print("Write a program that asks the user for a number and handles exceptions (e.g., ValueError) if the user enters something that's not a number.")

def main():
    number = only_number()
    print(f"Your choice of number is {number}.")   


def only_number():
    while True: 
        try:
            number = float(input("Enter your choice of number: "))
        except ValueError:
            print("Invalid number. Write only number.")
        else:
            return number
        

main()

         
     
    