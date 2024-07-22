import csv
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of orders to generate
num_orders = 50000

# Read existing orders to find the last order_id
last_order_id = 0
if os.path.exists('seeds/raw_orders.csv'):
    with open('seeds/raw_orders.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_order_id = max(last_order_id, int(row['order_id']))

# Generate order data
orders = []
for i in range(last_order_id + 1, last_order_id + num_orders + 1):
    order_date = fake.date_time_between(start_date='-1y', end_date='now')
    order = {
        'order_id': i,
        'customer_id': random.randint(1, 1000),  # Assuming 1000 customers
        'order_date': order_date.strftime('%Y-%m-%d'),
        'total_amount': round(random.uniform(10, 1000), 2)
    }
    orders.append(order)

# Append to CSV
with open('seeds/raw_orders.csv', 'a', newline='') as csvfile:
    fieldnames = ['order_id', 'customer_id', 'order_date', 'total_amount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header only if the file was empty
    if last_order_id == 0:
        writer.writeheader()
    
    for order in orders:
        writer.writerow(order)

print(f"{num_orders} new orders generated and appended to raw_orders.csv")