import re
import csv

with open('receipt.txt', 'r', encoding='utf8') as f:
    txt = f.read()

# txt = "null"

table = [['order', 'name', 'count', 'price', 'total_price']]

# product_patterns =

products_res = re.finditer(r'(?P<order>\d+).\n(?P<name>.+)\n(?P<count>\S+) x (?P<price>\S+)\n(?P<total_price>.+)', txt)

for res in products_res:
    table.append([
        res.group('order').strip(),
        res.group('name').strip(),
        res.group('count').strip(),
        res.group('price').strip(),
        res.group('total_price').strip()
    ])

# print(table)

with open('products.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(table)

