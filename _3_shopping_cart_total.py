#   3. Shopping Cart Total
#   A store needs a program to calculate the total cost of items. Write a progam that:
#   i. Accepts the prices of three items as inputs.
#   ii. Calculates and prints the total cost.

def shopping_cart_total():
    print("Shopping Cart Total")
    item1 = int(input("Enter the cost of the first item:   #"))
    item2 = int(input("Enter the cost of the second item:   #"))
    item3 = int(input("Enter the cost of the third item:   #"))
    
    total = item1+item2+item3
    
    print(f"Total Cost = #{total}")
    
    
shopping_cart_total()