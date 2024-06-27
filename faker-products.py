import csv
import random

# File name
file_name = 'products.csv'

# List of sample product names and categories
product_names = [
    "Smartphone", "Desk Chair", "Wireless Mouse", "Bluetooth Speaker", 
    "Laptop", "Coffee Maker", "Air Purifier", "Electric Kettle",
    "Headphones", "Fitness Tracker", "Monitor", "Tablet",
    "Gaming Console", "Smartwatch", "USB Drive", "Backpack",
    "Webcam", "Router", "LED Lamp", "External Hard Drive",
    "Projector", "Alarm Clock", "Fan", "Heater",
    "Blender", "Water Bottle", "Camera", "Microwave",
    "Oven", "Refrigerator", "Washing Machine", "Dishwasher",
    "Television", "Hair Dryer", "Iron", "Vacuum Cleaner",
    "Sewing Machine", "Printer", "Scanner", "Drone",
    "3D Printer", "Smart Thermostat", "Action Camera", "Electric Scooter",
    "VR Headset", "Tablet Stand", "Keyboard", "Drawing Tablet"
]

categories = ['Electronics', 'Furniture', 'Accessories', 'Home Appliances']

# Generate data for 50 products
num_products = 50
products = []

for i in range(num_products):
    product_id = i + 1
    product_name = random.choice(product_names)
    category = random.choice(categories)
    price = round(random.uniform(10.0, 1000.0), 2)  # Prices between $10 and $1000
    quantity = random.randint(1, 100)  # Quantity between 1 and 100
    rating = round(random.uniform(1.0, 5.0), 1)  # Rating between 1.0 and 5.0
    
    products.append([product_id, product_name, category, price, quantity, rating])

# Write to CSV
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Product ID', 'Product Name', 'Category', 'Price', 'Quantity', 'Rating'])
    # Write the product data
    writer.writerows(products)

print(f'{num_products} products have been written to {file_name}.')
