#   6. Currency Converter
#   Write a program that:
#       i.   Accepts an amount in dollars.
#       ii.  Converts it to Naira currency based on the current conversion rate.
#       iii. Prints the converted amount.

def currency_converter():
    print("Currency Converter Program: \n")
    dollars = float(input("Enter amount in dollars:   $"))
    exchange_rate_to_naira = 1600
    naira = dollars * exchange_rate_to_naira
    print(f"\n{dollars}dollars converts to #{naira}")
    
    
currency_converter()