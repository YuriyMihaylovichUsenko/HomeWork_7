# Task 1
sentence = input('Input some sentence of words')
unique_words = {}
for i in sentence.split():
    if i not in unique_words.keys():
        unique_words[i] = 1
    else:
        unique_words[i] += 1
print(unique_words)


# Task 2
def counter(dict_1, dict_2):
    print({key: dict_1[key]*dict_2[key] for key in dict_1})


counter({
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}, {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
})

# Task 3
print([(i, i*i) for i in range(1, 11)])
