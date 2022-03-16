import re


def multiple(nums: []) -> int:
    product = 1
    for n in nums:
        product *= n

    return product


product = multiple(
    list(
        map(
            int,
            re.findall(r'\d+', input("Write sequence of numbers separated by anything:\n")
            )
        )
    )
)
print(f'The product is {product}')
