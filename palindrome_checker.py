print("Write a program that checks if a given string is a palindrome (reads the same backward as forward).")

def palindrome (user_input):
    user_input = ''.join(filter(str.isalnum, user_input)).lower()

    #reversed_input = ''.join(reversed(user_input))

# Using slicind instead of reversed.
    return user_input == user_input[::-1]

user = input("Write string to to check if it is a palindrome: ")
if palindrome(user): 
    print(f"'{user}' is a Palindrome!")
 
else:
    print(f"'{user}' is not a Palindrome!")    



