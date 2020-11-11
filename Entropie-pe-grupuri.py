import math

#citim fișierul cu cele mai frecvente 8000 de cuvinte
file = open('comm_words.txt', encoding="utf8")
s = file.read()

def string_to_number(s): #funcție care transformă un șir de litere din limba română într-un unic număr natural
    l = len(s)
    power = value = 1
    result = 0
    s = s[:-l-1:-1] #inversăm șirul
    for letter in s:
        if letter == "ă":
            value = 27
        if letter == "â":
            value = 28
        if letter == "î":
            value = 29
        if letter == "ș":
            value = 30
        if letter == "ț":
            value = 31
        if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
            value = ord(letter) - ord("a") + 1
        result += power * value
        power *= 32
    return result

def number_to_string(nr): #funcție care transformă un număr natural într-un unic șir de litere din limba română
    new_word = ""
    while nr > 0:
        rest = nr % 32
        nr //= 32
        if rest == 31:
            letter = "ț"
        if rest == 30:
            letter = "ș"
        if rest == 29:
            letter = "î"
        if rest == 28:
            letter = "â"
        if rest == 27:
            letter = "ă"
        if rest >= 1 and rest <= 26:
            letter = chr(ord("a") + rest - 1)
        new_word = new_word + letter

    l = len(new_word)
    new_word = new_word[:-l-1:-1]
    return new_word

def fixed_string(l): #funcție care returnează entropia unei litere din limba română, utilizând grupuri de litere de lungime l
    global word_list
    import math

    sir1 = "a" * l
    sir2 = "ț" * l
    left = string_to_number(sir1)
    right = string_to_number(sir2)
    total = 0
    lista = word_list.split(" ")

    for i in range(left , right+1):
        if i == string_to_number(number_to_string(i)):
            substring = number_to_string(i)
            frequency = word_list.count(substring)
            total += frequency

    enthropy = 0

    for i in range(left , right+1):
        if i == string_to_number(number_to_string(i)):
            substring = number_to_string(i)
            frequency = word_list.count(substring)
            probability = frequency / total
            if probability > 0:
                enthropy -= probability * math.log2(probability)

    enthropy = enthropy / l

    return enthropy

def letter(ch): #funcție care returnează 1 dacă ch este literă din limba română și 0 în caz contrar
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

l = len(s)

# înlocuim aparițiile literei "î" din interiorul cuvintelor cu litera "â"
for i in range(1,l-1):
    if s[i] == "î" and letter(s[i-1]) == 1 and letter(s[i+1]) == 1:
        s = s[:i] + "â" + s[i+1:]

s = s.split("\n")
word_list = ""

#scoatem din fișierul citit cele 8000 de cuvinte și creăm un nou șir cu aceste cuvinte despărțite de spații
for current_word in s:
    current_word = current_word.replace("­" , "")
    current_word = current_word.replace("-", "") # eliminăm cratimele
    new_word = current_word.split(" ")
    word = new_word[0]
    word_list = word_list + word
    word_list = word_list + " "

print(fixed_string(1))
