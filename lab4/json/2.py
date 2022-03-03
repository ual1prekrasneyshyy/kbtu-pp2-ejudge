import json

required_attributes = ("dn", "descr", "speed", "mtu")

lengths_of_cells = {}


# Only necessary parameters

def count_length_of_cells(arr):
    data = arr["imdata"][0]["l1PhysIf"]["attributes"]
    for attr in required_attributes:
        length = 2
        key = attr
        value = data[key]
        if len(key) > len(value):
            if key == "descr":
                length += len("Description")
            else:
                length += len(key)
        else:
            length += len(value)
        lengths_of_cells[key] = length


class Interface:
    def __init__(self, dn, description, speed, mtu):
        self.dn = dn
        self.description = description
        self.speed = speed
        self.mtu = mtu

    def __str__(self):
        return f"{self.dn}{' ' * (lengths_of_cells['dn'] - len(self.dn))}{self.description}{' ' * (lengths_of_cells['descr'] - len(self.description))}{self.speed}{' ' * (lengths_of_cells['speed'] - len(self.speed))}{self.mtu}"


def generate_output_data(arr):
    for a in arr["imdata"]:
        i = a["l1PhysIf"]["attributes"]
        interface = Interface(i["dn"], i["descr"], i["speed"], i["mtu"])
        yield interface


with open("sample-data.json", "r") as f:
    input_data = f.read()

arr = json.loads(input_data)
count_length_of_cells(arr)

print("Interface Status")
print("=" * 100)
print(
    f"DN{' ' * (lengths_of_cells['dn'] - 2)}Description{' ' * (lengths_of_cells['descr'] - 11)}Speed{' ' * (lengths_of_cells['speed'] - 5)}MTU")
print(
    f"{'-' * 2}{' ' * (lengths_of_cells['dn'] - 2)}{'-' * 11}{' ' * (lengths_of_cells['descr'] - 11)}{'-' * 5}{' ' * (lengths_of_cells['speed'] - 5)}{'-' * 3}")

for i in generate_output_data(arr):
    print(i)
