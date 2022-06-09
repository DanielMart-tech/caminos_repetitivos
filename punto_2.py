# Program to calculate the velocity of a vehicle

print("Velocity")
distance = int(input("Distance: "))  / 1000 # Distance in meters. It is divided by 1000 to get the result in kilometers.
time = int(input("Time ")) / 3600 # Time in seconds. It is divided by 3600 to get the result in hours.
velocity = distance / time 

if velocity >= 1 and velocity <= 20:
    print("Warning! Slow velocity!")
elif velocity >= 21 and velocity <= 60:
    print("Normal velocity. This person is a good driver.")
elif velocity >= 61 and velocity <= 80:
    print("Warning! Fast velocity!")
elif velocity >= 81 and velocity <= 120:
    print("Fine Type I")    
elif velocity > 120:
    print("Fine Type II")

if velocity >= 81:
    alcohol_levels = int(input("Alcohol levels: "))
    if alcohol_levels >= 20 and alcohol_levels <= 39:
        print("Driver's license suspended between 6 and 12 months")
    elif alcohol_levels >= 40 and alcohol_levels <= 99:
        print("Driver's license suspended between 1 and 3 years")
    elif alcohol_levels >= 100 and alcohol_levels <= 149:
        print("Driver's license suspended between 3 and 5 years and they must attend workshops in rehabilitation centre for minimum 40 hours")
    elif alcohol_levels > 150:
        print("Driver's license suspended between 5 and 10 years and they must attend workshops in rehabilitation centre for minimum 80 hours")


