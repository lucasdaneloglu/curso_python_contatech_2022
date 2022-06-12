try:
    total_sales = int(input("Enter the total sales as integer: "))
    total_amount_sales = 0
    for sale_index in range(1, total_sales + 1):
        sale = int(input(f'Enter the {sale_index} sales amount as integer: '))
        total_amount_sales += sale
    print("The total amount of sales is: ", total_amount_sales)
except ValueError:
    print("Invalid input")
