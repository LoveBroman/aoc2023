import itertools
from functools import cmp_to_key

cs = []
with open("input_data/ex7_data") as data:
    for row in data:
        cs.append(row.strip())

vs = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
#vss = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
vvals = dict()
for i, v in enumerate(vs):
    vvals[v] = i
vvals["J"] = 20


class Hand:
    def __init__(self, h, r):
        self.h = h
        self.r = r
        self.v = 0
        self.atts = self.get_atts()

    def get_atts(self):
        ps = {c: 0 for c in self.h}
        for i, c in enumerate(self.h):
            ps[c] += 1
        pss = list(ps.values())
        return list(filter(lambda x: x > 0, pss))

    def get_label(self):
        d = self.atts
        if len(d) == 1:
            return 0
        elif len(d) == 2:
            if max(d) == 4:
                return 1
            else:
                return 2
        elif len(d) == 3:
            if max(d) == 3:
                return 3
            else:
                return 4
        elif len(d) == 4:
            return 5
        else:
            return 6

    def corr_lbl(self):
        l = self.get_label()
        for c in self.h:
            if c == "J":
                if l == 6:
                    l = 5
                elif l == 5:
                    l = 3
                elif l == 4:
                    l = 2
                elif l == 3:
                    l = 1
                elif l == 2:
                    l = 1
                elif l== 1:
                    l = 0
        return l


    def to_vlist(self):
        return [vvals[c] for c in self.h]

def parse_data(cs):
    hs = []
    for i, p in enumerate(cs):
        h, r = p.split()
        hi = Hand(h, int(r))
        hs.append(hi)
    return hs

def complist(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return l1[i]- l2[i]
    return l1 < l2


def compfunc1(h1, h2):
    # print(h1.h, h1.get_label())
    # print(h2.h, h2.get_label())
    if abs(h1.corr_lbl() - h2.corr_lbl()) > 0.5:
        return h2.corr_lbl() - h1.corr_lbl()
    else:
        return complist(h2.to_vlist(), h1.to_vlist())


def handle_hs(hs):
    res = 0
    shs = sorted(hs, key=cmp_to_key(compfunc1))
    for i, h in enumerate(shs):
        print(h.h, h.to_vlist(), h.corr_lbl())
        h.v = i + 1
    sv = sorted(shs, key = lambda h: h.r * h.v)
    for i,h in enumerate(sv):
        #print(h.h, h.r * h.v, h.r, h.v)
        res += h.r * h.v
    print(res)

sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
smpl = [s.strip() for s in sample.split("\n")]


hs = parse_data(cs)
handle_hs(hs)


