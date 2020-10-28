import math

file = open('comm_words.txt', encoding="utf8")
s = file.read()
s = s.split("\n")
word_list = dict()

med_len = float(0)

let_freq = []
total_let_freq = 0
for i in range(31):
    let_freq.append(0)

for word in s: # aici o sa fie cate cuvinte bagam, inputul l-am presupus a fi de forma cuvant frecventa
    new_word = word.split(" ")
    #print(new_word[0], new_word[2])
    real_word = new_word[0]
    frequency = int(new_word[1])
    med_len = med_len  + len(real_word)

    for l in real_word:
        if l >= 'a' and l <= 'z':
            let_freq[ord(l)-ord('a')] += 1
        else:
            if l == 'ă': let_freq[30] += 1
            if l == 'â': let_freq[29] += 1
            if l == 'î': let_freq[28] += 1
            if l == 'ș': let_freq[27] += 1
            if l == 'ț': let_freq[26] += 1
    total_let_freq += len(real_word)

    # print(real_word, end = '\n')
    # print(frequency, end = '\n')
    word_list[real_word] = frequency
med_len = med_len/8000
sum = 0

for key in word_list:
    sum = sum + word_list[key]

expected_value = 0

for key in word_list:
    #print(word_list[key]), "->", print(sum)
    ratio = sum / word_list[key]
    #print(1/ratio)
    expected_value = expected_value + (1/ratio) * math.log2(ratio)
    #print(len(key), "->" , word_list[key])

print("Entropia limbii române este:", expected_value)
