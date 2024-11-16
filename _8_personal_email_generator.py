#   8. Personalized Email Generator
#   
#   Create a program that:
#   i. Prompts the user for their name and department.
#   ii. Generates and prints a sample email in the format: "Dear [Name], welcome to the [Department] team!".

def email_generator():
    name = input("Enter your Name:  ")
    dept = input("Enter your Department:  ")
    
    sample_mail = f"Dear {name}, welcome to the {dept} team!"
    print(sample_mail)
    
email_generator()