#   2. Swapping Variables
#   A logistics company needs to switch values between two storage units. Write a program that:
#   Takes two inputs, unit1 and unit2.
#   Swaps their values and prints the updated results.

def swapper():
    unit1 = input("Enter unit 1: \t")
    unit2 = input("Enter unit 2: \t")
    
    value2 = unit1
    value1 = unit2
    
    unit1=value1
    unit2=value2
    
    print("\nHere are the swapped values:")
    print(f"unit 1 = {unit1}\nunit 2 = {unit2}")
    
swapper()