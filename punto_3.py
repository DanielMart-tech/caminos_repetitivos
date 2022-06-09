#Program to calculate the distance reached every second by an object thrown from a building 

"""
Equation: d = (g * t**2) / 2
Isolate 't' variable: t = ((2 * d) / g)**1/2
"""

height = float(input("Please, introduce the height in meters: "))
g = 9.8

while height >= 0:
    time = ((2 * height) / g)**(1/2)
    print(f"Distance: {height} ; Time: {time}")
    height -= 1
    