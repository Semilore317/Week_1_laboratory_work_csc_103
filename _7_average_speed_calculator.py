#   7.Average Speed Calculator
#   A travel app needs to calculate the average speed of a trip. Write a program that:
#       i. Takes the distance (in kilometers) and time (in hours) as inputs.
#       ii. Calculates and prints the average speed (distance/time).

def average_speed_calculator():
    distance = float(input(f"Enter distance in km: "))
    time = float(input(f"Enter time in hours: "))
    
    avg_speed = distance / time
    
    print(f"Average Speed is {avg_speed}km/h")
    
    
average_speed_calculator()