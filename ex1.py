
ws = []
with open("input_data/ex1_data") as data:
    for row in data:
        ws.append(row)

print(ws)


def search_letters(word):
    frst = ""
    end = ""
    for l in word:
        if l.isdigit():
            frst = l
            break
    for l in word[::-1]:
        if l.isdigit():
            end = l
            break
    return int(frst + end)

letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def beginning(w1, w2):
    for i, l in enumerate(w1):
        if not (w1[i] == w2[i]):
            return False
    return True

def look_for_word(word, letters):
    s = ""
    for i, l in enumerate(word):
        if i == 15:
            pass
        if l.isdigit():
            return l
        s += l
        while len(s) != 0:
            fl = list(filter(lambda x: beginning(s, x), letters))
            if len(fl) == 0:
                s = s[1:]
            else:
                break
        if len(s) == 0:
            s = l
        if s in letters:
            return str(letters.index(s) + 1)

def look_for_wl(word, letters):
    letrev = [w[::-1] for w in letters]
    frst = look_for_word(word, letters)
    end = look_for_word(word[::-1], letrev)
    return int(frst + end)



valsum = sum([search_letters(w.strip()) for w in ws])
#print(valsum)

with_words = [look_for_wl(w, letters) for w in ws]
#print(sum(with_words))

for i in list(zip(with_words, ws)):
    print(i)
print(sum(with_words))

w = look_for_wl("jffvtzkbjnkdtvfsfthree431lrpgmtv", letters)
print(w)
#print(beginning("thr", "three"))
