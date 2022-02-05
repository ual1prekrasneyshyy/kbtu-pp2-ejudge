def number_is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


input_data = input()  #2 numbers n and f are written in one line
input_data = input_data.split(" ")
n = int(input_data[0])   #n is the first
f = int(input_data[1])   #f is the second
if 1 <= n <= 1000 and 1 <= f <= 1000:
    is_guaranteed_to_hit_the_target = False
    if f % 2 == 0 and number_is_prime(n) and n < 500:
        is_guaranteed_to_hit_the_target = True

    if is_guaranteed_to_hit_the_target:
        print("Good job!")
    else:
        print("Try next time!")