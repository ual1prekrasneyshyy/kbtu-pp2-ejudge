import re

camel = input("Write in camel case:\n")

snake = re.search(r'[a-z]+', camel).group()  #first word

other_words = re.findall('[A-Z][a-z]+', camel)

for w in other_words:
    snake += '_'
    for i in range(len(w)):
        if i == 0:
            snake += w[i].lower()
        else:
            snake += w[i]

print("Snake case:")
print(snake)

