#   9. Weekly Salary Calculator

#   Write a program that:
#   i. Declares variables for hourly_rate and hours_worked.
#   ii. Calculates and prints the weekly salary.

def weekly_salary_calculator():
    hourly_rate = int(input("Enter the hourly rate:  $"))
    hours_worked = int(input("Enter the weekly hours worked:   "))
    
    weekly_salary = hourly_rate * hours_worked
    
    print(f"Weekly Salary is ${weekly_salary}")
    
    
weekly_salary_calculator()