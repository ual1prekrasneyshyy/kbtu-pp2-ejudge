import re
import csv

with open('receipt.txt', 'r') as f:
    txt = f.read()

# txt = "null"

table = [['order', 'name', 'count', 'price', 'total_price']]

product_patterns = r'<order>.+.\n<name>.+\n<count>.+ x <price>.+\n<total_price>.+'

products_res = re.finditer(product_patterns, txt)

for res in products_res:
    table.append([
        res.group('order').strip(),
        res.group('name').strip(),
        res.group('count').strip(),
        res.group('price').strip(),
        res.group('total_price').strip()
    ])

with open('products.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(table)

