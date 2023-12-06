rs = ""
with open("input_data/ex6_data") as data:
    for row in data:
        rs += row

print(rs)
def clean_input(rs):
    ts, ds = rs.strip().split("\n")
    ts = list(map(lambda y: int(y), list(filter(lambda x: len(x) != 0, ts.split("    ")[1:]))))
    ds = list(map(lambda x: int(x), ds.split("   ")[1:]))
    return ts, ds

def possible_sols(t, d):
    x = 1
    j = 0
    res = x*(t-x) - d
    s = True
    while s or res > 0:
        if res > 0:
            s = False
            j += 1
        x += 1
        res = x * (t - x) - d
    return j


ts, ds = clean_input(rs)
res = 1
for i in range(len(ts)):
    j = possible_sols(ts[i], ds[i])
    res *= j
print(res)

ts2 = int("".join(list(map(lambda x: str(x), ts))))
ds2 = int("".join(list(map(lambda x: str(x), ds))))
print(possible_sols(ts2, ds2))

