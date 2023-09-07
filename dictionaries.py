print("Create a dictionary that stores the names and ages of your family members. Retrieve and print the age of a specific family member.")

family_dict = {
    "Bhanubhai" : 52,
    "Bhavnaben" : 50,
    "Pooja" : 28,
    "Shrujal" : 27,
    "Henish" : 25

}

family_mem = input("Enter specific family member's name: ").capitalize()

if family_mem in family_dict:
    age = family_dict[family_mem]
    print(f"{family_mem}'s age is {age}.")
else:
    print(f"{family_mem} is not in the list. Try again.")


