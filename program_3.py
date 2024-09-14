def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    print("Please input the name and price of the item you are purchasing below when prompted.")
    item1 = input('Item 1: ')
    price1 = input('Item 1 Price: $')
    print(item1, price1)
    item2 = input('Item 2: ')
    price2 = input('Item 2 Price: $')
    print(item2, price2)
    item3 = input('Item 3: ')
    price3 = input('Item 3 Price: $')
    print(item3, price3)
    item4 = input('Item 4: ')
    price4 = input('Item 4 Price: $')
    print(item4, price4)
    item5 = input('Item 5: ')
    price5 = input('Item 5 Price: $')
    print(item5, price5)
    item_subtotal = (price1 + price2 + price3 + price4 + price5)
    print('Subtotal: $', str(item_subtotal))
    sales_tax = float(item_subtotal * int(7 / 100))
    print('Sales Tax: $', str(sales_tax))
    sales_total = (item_subtotal + sales_tax)
    print('Sale Total: $', float(sales_total))

calculate_total_purchase()

calculate_total_purchase()
