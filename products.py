import csv

def read_csv(file_name):
    # Open the CSV file for reading
    yield from open(file_name,'r', newline='', encoding='utf-8')

    """with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            yield row"""
            
# Create an iterator for the CSV rows
product_iterator = iter(read_csv("products.csv"))
print(product_iterator)

# Example of iterating over the CSV rows
for row in product_iterator:
    print(row)
