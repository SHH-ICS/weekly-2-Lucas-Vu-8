import math

def calculate_circle_properties():
    diameter = input("Enter the diameter of the circle: ")
    try:
        diameter = float(diameter)
    except ValueError:
        print("Error: Please enter a valid number.")
    if diameter < 0:
        print("Error: Diameter cannot be negative. Please enter a valid value.")
        return 
    radius = diameter / 2
    circumference = math.pi * diameter
    area = math.pi * radius ** 2
    print(circumference)
    print(area)

calculate_circle_properties()
