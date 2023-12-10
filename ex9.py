cs = []
with open("input_data/ex9_data") as data:
    for row in data:
        cs.append(row.strip())

sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split("\n")

class OasSeq:
    def __init__(self, r):
        self.r = r
        self.rs= [r]

    def __str__(self):
        res = ""
        for seq in self.rs:
            res += "\n"
            res += " " + str(seq) + " "

        return res

    @staticmethod
    def diffs(l):
        lres = []
        for i in range(1, len(l)):
            lres.append(l[i] - l[i-1])
        return lres

    def reduce(self):
        nz = any(self.r)
        i = 0
        while nz:
            diff = self.diffs(self.rs[i])
            self.rs.append(diff)
            i += 1
            nz = any(self.rs[i])

    def extrapolate(self):
        self.rs[-1].append(0)
        last = 0
        for i in range(2, len(self.rs) + 1):
            sl = self.rs[(len(self.rs) - i)][-1]
            last = sl + last
            self.rs[len(self.rs) - i].append(last)

    def baxtrapolate(self):
        self.rs[-1] = [0] + self.rs[-1]
        last = 0
        for i in range(2, len(self.rs) + 1):
            sl = self.rs[(len(self.rs) - i)][0]
            last = sl - last
            self.rs[len(self.rs) - i] = [last] + self.rs[len(self.rs) - i]



    def ext_val(self):
        return self.rs[0][-1]

    def baxt_val(self):
        return self.rs[0][0]



def parse_data(data):
    seqs = []
    for i, r in enumerate(data):
        elems = list(map(lambda x: int(x), r.split()))
        seqs.append(OasSeq(elems))
    return seqs

seqs = parse_data(cs)
def ex1():
    i = 0
    for seq in seqs:
        seq.reduce()
        seq.extrapolate()
        i += seq.ext_val()
    print(i)

def ex2():
    i = 0
    for seq in seqs:
        seq.reduce()
        seq.baxtrapolate()
        i += seq.baxt_val()
    print(i)

ex2()