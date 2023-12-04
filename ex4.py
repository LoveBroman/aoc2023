import re
cs = []
with open("input_data/ex4_data") as data:
    for row in data:
        cs.append(row.strip())

def clean_card(card):
     split = re.split(':|\|', card)
     win = split[1]
     y = split[2]
     ws = set([int(i) for i in win.split()])
     yl = [int(n) for n in y.split()]
     return ws, yl

def proc_card(ws, yl):
    i = 0
    for n in yl:
        if n in ws and i == 0:
            i = 1
        elif n in ws:
            i *= 2
    return i

def proc_card2(ws, yl, cops, i):
    j = 1
    for n in yl:
        if n in ws:
            cops[i + j] += 1
            j += 1
    return i

def clean_input(cs):
    res = 0
    for card in cs:
        ws, yl = clean_card(card)
        res += proc_card(ws, yl)
    return res

def card_game(cs):
    ccops = [1] * len(cs)
    for i, c in enumerate(cs):
        ws, yl = clean_card(c)
        for j in range(ccops[i]):
            proc_card2(ws, yl, ccops, i)
    return ccops

res = clean_input(cs)
res2 = card_game(cs)