# find total sales revenue for a specific product from the csv file

import csv

def total_sales_revenue(product_name):
    total_revenue = 0
    with open('sales_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader: 
            if row['product'] == product_name:
                total_revenue += float(row['sales_revenue'])
    return total_revenue

product_name = 'Product A'
total_revenue = total_sales_revenue(product_name)
print(f"Total sales revenue for {product_name}: {total_revenue}")