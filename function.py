print("Write a function that calculates the area of a rectangle given its length and width as parameters.")

def rectangle(length_width):
    print(f"Area = {length_width}")


w= float(input("Enter width of rectangle: ")) 
l = float(input("Enter length of rectangle: "))
rectangle (w*l)  


#anotherway to write this code.
def rectangle(length, width):
    area = length * width
    print(f"Area = {area}")

W = float(input("Enter width of rectangle: ")) 
L = float(input("Enter length of rectangle: "))
rectangle(L, W)