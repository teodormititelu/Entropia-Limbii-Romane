import collections

#citim fișierul
file = open('inputt.txt', encoding="utf8")
s = file.read()
n = int(input("Scrieți numărul de litere:"))

def cifra(c): #funcție care returnează 1 dacă c este cifră
    if ord(c) >= ord("0") and ord(c) <= ord("9"):
        return 1
    return 0

def litera(ch): #funcție care returnează 1 dacă ch este literă din limba română și 0 în caz contrar
    if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
        return 1
    if ch == "ă":
        return 1
    if ch == "î":
        return 1
    if ch == "â":
        return 1
    if ch == "ș":
        return 1
    if ch == "ț":
        return 1
    return 0

words = ""

def find_enthropy(nr):
    import math
    global word_list
    global l

    for i in range(0 , l-nr+1):
        substring = words[i:i+nr]
        if substring in word_list:
            word_list[substring] += 1
        else:
            word_list[substring] = 1

    enthropy = 0
    total = l - nr + 1

    for x in word_list.values():
        probability = x / total
        if probability > 0:
            enthropy -= probability * math.log2(probability)

    enthropy = enthropy / nr

    return enthropy

for word in s.lower().split():
    if word == "—" or word == "–" or word == " " or word == "":
        continue
    if word == "\n" or word == "\0":
        continue
    if cifra(word[0]) == 1:
        continue

    word = word.replace("_", "")
    word = word.replace("—", "")
    word = word.replace("", "")
    word = word.replace("“", "")
    word = word.replace("„", "")
    word = word.replace("-", "")
    word = word.replace(".", "")
    word = word.replace(" ", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace('"', "")
    word = word.replace("!", "")
    word = word.replace("*", "")
    word = word.replace(";", "")
    word = word.replace("/", "")
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("”", "")
    word = word.replace("­", "")
    if len(word) < 2:
        continue
    words += word
    words += " "

l = len(words)

# înlocuim aparițiile literei "î" din interiorul cuvintelor cu litera "â"
for i in range(1,l-1):
    if words[i] == "î" and litera(words[i-1]) == 1 and litera(words[i+1]) == 1:
        words = words[:i] + "â" + words[i+1:]

word_list = dict()

print("Entropia limbii române este" , find_enthropy(n))
