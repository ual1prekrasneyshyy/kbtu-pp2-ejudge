import json

with open("sample-data.json", "r") as f:
    data = f.read()

data = json.loads(data)
output_data = "Interface status\n"
output_data += "="*540+"\n"
# output_data += "\n"+f"Total count: {data['totalCount']}\n"

obj1 = data["imdata"][0]["l1PhysIf"]["attributes"]
header_of_table = ""
header_of_table_1 = ""

lengths_of_cells_of_table = {}

for key, value in obj1.items():
    length_of_cell = 3
    if len(key) > len(value):
        length_of_cell += len(key)
    else:
        length_of_cell += len(value)
    lengths_of_cells_of_table[key] = length_of_cell
    header_of_table += f'{key}{" "*(length_of_cell - len(key))}'
    header_of_table_1 += f'{"-"*(length_of_cell - 2)}{" "*2}'


output_data += header_of_table + "\n"
output_data += header_of_table_1 + "\n"

for obj in data['imdata']:
    obj = obj["l1PhysIf"]["attributes"]
    data_to_print = ""

    for key, value in obj.items():
        data_to_print += f"{value}{' '*(lengths_of_cells_of_table[key]-len(value))}"
    output_data += data_to_print + "\n"


with open("output.txt", "w") as f:
    f.write(output_data)

print("Table is saved in file!")
