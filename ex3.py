ls = []
js = ""

with open("input_data/ex3_data") as data:
    for row in data:
        ls.append(row)
        js += row
# print(len(ls[0]))
# print(len(ls[1]))
# print(len(ls[2]))
#Kan testa droppa \n om det leder till fel
def get_symbols(js):
    return set(filter(lambda x: not (x.isdigit() or x == "."), js))

def in_range(ls, ind, in_combs):
    def criteria(x):
        return (x[0] + ind[0] < len(ls)) and (x[0] + ind[0] >= 0) and (x[1] + ind[1] < len(ls[0])) and (x[1] + ind[1] >= 0)
    return list(filter(criteria, in_combs))

def is_adjancent(ls, ind, sym_set):
    if ind == (127, 139):
         pass
    indy, indx = ind[0], ind[1]
    in_combs = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]
    in_combs = in_range(ls, ind, in_combs)
    for ip in in_combs:
        if ls[indy + ip[0]][indx + ip[1]] in sym_set:
            return True
    return False

def get_number(ls, ind, stop_set):
    i = 0
    num = []
    indx, indy = ind[1], ind[0]
    num += ls[indy][indx]
    stop_set.add((indy, indx))
    while True:
        i += 1
        if (indy,indx + i) in stop_set:
            return 0
        adj = ls[indy][indx + i]
        if adj.isdigit():
            stop_set.add((indy, indx + i))
            num += [adj]
        else:
            break
    i = 0
    while True:
        i -= 1
        if (indy,indx + i) in stop_set:
            return 0
        adj = ls[indy][indx + i]
        if adj.isdigit():
            stop_set.add((indy, indx + i))
            num = [adj] + num
        else:
            break
    result = int("".join(num))
    if result == 996:
        pass
    return result


sym_set = get_symbols(js)
sym_set.remove("\n")
sample = list(filter(lambda x: len(x) != 0, """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")))

def ex1(input):
    #print(len(input), len(input[0]))
    stop_set = set()
    parts = []
    deb = []
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if input[i][j].isdigit():
                if is_adjancent(input, (i, j), sym_set):
                    number = get_number(input, (i, j), stop_set)
                    parts.append(number)
                    deb.append(input[i][j])

    return parts, sum(parts)

parts , sum  = ex1(ls)
print(sum)

