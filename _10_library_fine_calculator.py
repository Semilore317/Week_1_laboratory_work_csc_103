#   10. Library Fine Calculator
#   A library wants to calculate overdue fines. Write a program that:
#       i.  Takes the number of overdue days as input.
#       ii. Calculates the fine at $0.50 per day and prints the result.


def fine_calculator():
    print("Library Fine Calculator")
    days_overdue = int(input("Enter the number of overdue days: "))
    fine_per_day = 0.50
    
    total_fine = days_overdue * fine_per_day
    
    print(f"Fine is ${total_fine}") 
    
fine_calculator()