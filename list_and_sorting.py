print("Create a list of numbers, sort them in ascending and descending order, and print the results.\n")

#numbers = [5,23,17,65,1,98,125,365,47,12,2587,3698,14785,25631,985,425]
#print("List of the Numbers!", numbers)
user_input = input("Enter your list of numbers which you want to sort it out: ")

numbers = [int(num) for num in user_input.split()]

ascending_order = sorted(numbers)
print("Let's sort it out in Ascending Order: ",ascending_order)

descending_order = list(reversed(ascending_order))
print("Let's sort it out in Descending Order: ", descending_order)
