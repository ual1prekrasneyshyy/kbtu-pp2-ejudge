def generate_even_numbers(n):
    i = 0
    while i <= n:
        if i == n or i+1 == n:
            yield str(i)
        else:
            yield f'{i},'
        i += 2


n = int(input("Write some number:\n"))

output_data = ""
for i in generate_even_numbers(n):
    output_data += i

print(output_data)