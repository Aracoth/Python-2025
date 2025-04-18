from pprint import pprint

# which character occurs most?
sentence = "This is a common interview question"
# a dictionary to store characters(key) and their occurances(value)
char_frequency = {}
# check if char in sentence is in my dict.
for char in sentence:
    # if it IS in my dict, add a count of 1 to the dict.
    if char in char_frequency:
        # the [char] is to access the char data(count)
        char_frequency[char] += 1
    else:
        # if the char is not in dict. the char = 1
        char_frequency[char] = 1

print(char_frequency)


char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True
)
print(char_frequency_sorted[0])
