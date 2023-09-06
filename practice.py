#Practice of conditional statement: 
def person_age(its):
    print(f"Your age is {its}")

age = int(input("What's your age? : , "))
person_age(age)

if age <= 17:
    print("So, you are MINOR!")
else:
    print("So, you are ADULT!")    