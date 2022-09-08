sentence = "Thisisacommoninterviewquestion"

# Solution 1
item_set = {}
max_num = 0
max_item = ''
for item in sentence:
    if item in item_set:
        item_set[item] = item_set[item] + 1
        if item_set[item] > max_num:
            max_num = item_set[item]
            max_item = item
    else:
        item_set[item] = 1

print(max_num, max_item)

# Solution 2
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])