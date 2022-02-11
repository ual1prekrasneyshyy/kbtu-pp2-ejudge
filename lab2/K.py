words = set(input().split(" ")) #We are intersting in unique words

words = list(words)
words.sort()

print(len(words))

for word in words:
    print_unique_word = ""
    for c in word:
        if c != ',' and c != '.' and c != '?' and c != '!':
            print_unique_word += c
    print(print_unique_word)