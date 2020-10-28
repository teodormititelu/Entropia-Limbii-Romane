import collections

#deschidem fisier de input
file = open('input.txt', encoding="utf8")
s = file.read()

#hash-ul de cuvinte
word_hash = {} 

#eliminam semnele de punctuatie
for word in s.lower().split():
    if word == "—" or word == "–" or word == " " or word == "": continue
    if word == "\n" or word == "\0": continue
    if len(word) < 2: continue
    word = word.replace("","")
    word = word.replace("“","")
    word = word.replace("„","")
    #word = word.replace("-","")
    word = word.replace(".","")
    word = word.replace(" ","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("*","")
    word = word.replace(";","")
    word = word.replace("/","")
    word = word.replace("[","")
    word = word.replace("]","")
    word = word.replace("(","")
    word = word.replace(")","")
    word = word.replace("?","")
    word = word.replace("!","")
    if word not in word_hash:
        word_hash[word] = 1
    else:
        word_hash[word] += 1

# Scrie in fisierul "comm_words.txt" cele mai frecvente N cuvinte
# n = int(input("Introdu valoarea N: "))
#print("\nCele mai frecvente N cuvinte sunt:\n")
n = 8000

g = open("comm_words.txt", "wb")

word_hash = collections.Counter(word_hash)
for word, count in word_hash.most_common(n):
    g.write(word.encode("utf-8"))
    g.write(" ".encode("utf-8"))
    g.write(str(count).encode("utf-8"))
    g.write("\n".encode("utf-8"))

g.close()
