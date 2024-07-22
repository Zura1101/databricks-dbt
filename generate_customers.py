import csv
import random
import os
from faker import Faker

fake = Faker()

# Number of customers to generate
num_customers = 10000

# Read existing customers to find the last customer_id
last_customer_id = 0
if os.path.exists('seeds/raw_customers.csv'):
    with open('seeds/raw_customers.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_customer_id = max(last_customer_id, int(row['customer_id']))

# Generate customer data
customers = []
for i in range(last_customer_id + 1, last_customer_id + num_customers + 1):
    customer = {
        'customer_id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'updated_at': fake.date_time_this_year().isoformat()
    }
    customers.append(customer)

# Append to CSV
with open('seeds/raw_customers.csv', 'a', newline='') as csvfile:
    fieldnames = ['customer_id', 'first_name', 'last_name', 'email', 'updated_at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header only if the file was empty
    if last_customer_id == 0:
        writer.writeheader()
    
    for customer in customers:
        writer.writerow(customer)

print(f"{num_customers} new customers generated and appended to raw_customers.csv")