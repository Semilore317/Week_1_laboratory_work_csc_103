#   5. Temperature Conversion
#   Create a program that:
#   Takes a temperature in Celsius as input.
#   i.  Converts it to Fahrenheit using the formula: F = C * 9/5 + 32.
#   ii. Prints the Fahrenheit equivalent.

def temperature_converter():
    celsius = int(input("Enter temperature in Celsius:   "))
    fahrenheit = celsius * 9/5 +32
    print(f"\nTemperature in Farenheit is {fahrenheit}F")
    
    
    
temperature_converter()