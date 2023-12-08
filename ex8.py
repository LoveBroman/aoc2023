import queue

cs = []
with open("input_data/ex8_data") as data:
    for row in data:
        cs.append(row.strip())

def clean_data(data):
    data = list(filter(lambda x: len(x) != 0, data))
    #print("\n".join(data))
    stps = data[0]
    dlist = dict()
    rest = data[1:]
    print(rest)
    for i, p in enumerate(rest):
        m = p.split(" = ")
        v = m[1].split(", ")
        l, r = v[0][1:], v[1][:-1]
        print(p, m[0], l, r)
        dlist[m[0]] = (l, r)
    adj = dict()
    nxt = None
    for key, value in dlist.items():
        nxt = key
        for s in stps:
            if s == "L":
                nxt = dlist[nxt][0]
            elif s == "R":
                nxt = dlist[nxt][1]
        adj[key] = [nxt]
    return adj, len(stps)

def BFS(G, root):
    Q = queue.Queue()
    expl = {i: 10e7 for i in list(G.keys())}
    expl[root] = 0
    Q.put(root)

    trav = list()
    while not Q.empty():
        v = Q.get()

        trav.append(v)
        for i in G[v]:
            print(i)
            if i in expl.keys():
                if expl[i] > 10e6:
                    expl[i] = 1 + expl[v]
                    Q.put(i)
    return expl, trav

sample = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split("\n")


adj, stps = clean_data(cs)

expl, trav = BFS(adj, "AAA")
print(expl["ZZZ"] * stps)
