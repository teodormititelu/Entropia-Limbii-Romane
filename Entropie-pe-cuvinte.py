import math

# citim cuvintele din fișier
file = open('comm_words.txt', encoding="utf8")
s = file.read()
s = s.split("\n")
word_list = dict()

med_len = float(0)

for word in s:
    new_word = word.split(" ")
    real_word = new_word[0]
    frequency = int(new_word[2])
    med_len = med_len + len(real_word)

    word_list[real_word] = frequency

med_len = med_len/8000
sum = 0

for key in word_list:
    sum = sum + word_list[key]

expected_value = 0

for key in word_list:
    ratio = sum / word_list[key]
    expected_value += (1/ratio) * math.log2(ratio)

print("Entropia pe cuvinte a limbii române este:", expected_value)

expected_value = expected_value / med_len

print("Entropia limbii române este:", expected_value)
