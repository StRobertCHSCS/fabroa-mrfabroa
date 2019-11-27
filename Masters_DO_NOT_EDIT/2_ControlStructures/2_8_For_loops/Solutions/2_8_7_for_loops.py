"""Write a cash register program that allows the user to enter the price AND quantity for 3 products.  
Output the total cost with 13% tax applied rounded to 2 decimals.  
(use `round(num,2)` to round `num` to 2 decimal places )"""

# initialize the total
total = 0

# get the products and quantity and add them to the total
for i in range (1, 4):
    price = float(input("Enter the price of product " + str(i) + ": "))
    qty = int(input("Enter the quantity of product " + str(i) + ": "))

    total = total + (price * qty)

print(round(total,2))


