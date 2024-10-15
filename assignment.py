import math

def calculate_circle_properties():
    # Get the diameter from the user
    diameter = float(input("Enter the diameter of the circle: "))
    if diameter < 0:
        print("Error: Diameter cannot be negative. Please enter a valid value.")
        return 
    radius = diameter / 2
    circumference = math.pi * diameter
    area = math.pi * radius ** 2
    print(circumference)
    print(area)

# Call the function
calculate_circle_properties()
