import re

ls = []

with open("input_data/ex2_data") as data:
#     data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    for row in data:
        ls.append(row.strip())

print(ls)

def filt_func(ls, w):
    filtered = list(filter(lambda x: x.find(w) != -1, ls))
    filt2 = [int("".join(list(filter(lambda x: x.isdigit(), s)))) for s in filtered]
    return filt2
def process_game(gs):
    ss = re.split(',|;|:', gs)
    inds = int("".join(list(filter(lambda c: c.isdigit(), ss[0]))))
    clrs = ["red", "blue", "green"]
    clr_dict = dict(zip(clrs, [0, 0, 0]))
    for c in clrs:
       clr_dict[c] = filt_func(ss[1:], c)
    return inds, clr_dict

def flw_rule(dct, rules):
    for key in dct.keys():
        print(dct[key], key, rules[key])
        breaks = list(filter(lambda x: x > rules[key], dct[key]))
        if len(breaks) != 0:
            print(breaks, key, "breaked Rule", rules[key])
            return False
    return True
rules = {"red": 12, "blue": 14, "green": 13}

summ = 0
for s in ls:
    print(s)
    inds, clr_dict = process_game(s)
    if flw_rule(clr_dict, rules):
        summ += inds
print(summ)