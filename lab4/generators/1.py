def generate_squares(limit: int):
    x = 1
    while x <= limit:
        yield f"x={x}, x^2={pow(x, 2)}"
        x += 1


lim = int(input("Input some number:\n"))

for num in generate_squares(lim):
    print(num)