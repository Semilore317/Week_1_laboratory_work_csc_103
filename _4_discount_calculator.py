#   4. Discount Calculator
#   An e-commerce site offers discounts to customers. Create a program that:   
#       i. Accepts the original price and discount percentage as inputs.
#       2. Calculates and prints the discounted price.

def discount_calculator():
    original_price = int(input("Enter original price:   #"))
    discount = int(input("Enter discount percentage:   #")) / 100
    
    discounted_price = original_price - (original_price * discount)
    
    print(f"Discounted_price is {discounted_price}")
    
discount_calculator()