#Practice of for loop!
def fav_fruits(number):
    print(f"Pick your favorite fruit from {number}")

fruits = ["Mango", "Watermelon", "Apple", "Ice Apple", "Orange"]
fav_fruits(fruits)

for fruit in fruits:
     user_input =input(f"My favorite fruit is ").capitalize()
     if user_input not in fruits:
          print("Invalid choice, please pick from the list.")
     else:
          
          break
    

     