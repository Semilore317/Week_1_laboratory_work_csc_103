#   Personal Greeting
#   A company wants a program that greets customers by their names. Write a program that:
#   Prompts the user for their name.
#   Prints a personalized greeting such as: "Hello, [name]! Welcome to our store."


def personal_greeting():
    name = input("Welocome to our company!\nPlease input your name: \n\n")
    print(f"\nHello, {name}!, Welcome to our store.")
    
personal_greeting()