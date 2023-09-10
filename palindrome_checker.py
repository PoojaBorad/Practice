print("Write a program that checks if a given string is a palindrome (reads the same backward as forward).")

def palindrome (user_input):
    user_input = user_input.replace(" ", " ").lower()

    #reversed_input = ''.join(reversed(user_input))

# Using slicind instead of reversed.
    return user_input == user_input[::-1]

user = input("Write string to which is Palindrome or not: ")
if palindrome(user): 
    print(f"'{user}' is a Palindrome!")
 
else:
    print(f"'{user}' is not a Palindrome!")    



