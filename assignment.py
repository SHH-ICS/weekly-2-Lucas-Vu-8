import math

def calculate_circle_properties():
    while True:
        diameter = input("Enter the diameter of the circle: ")
        try:
            diameter = float(diameter)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue 

        if diameter < 0:
            print("Error: Diameter cannot be negative. Please enter a valid value.")
            continue  

        radius = diameter / 2
        circumference = math.pi * diameter
        area = math.pi * radius ** 2

        print(circumference)
        print(area)
        
        another = input("Would you like to calculate another circle").lower()
        if another != 'yes':
            print("bye")
            break

calculate_circle_properties()
