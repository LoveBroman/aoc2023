import numpy as np
import copy
from time import time
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dists = []

    def __str__(self):
        return f"Pos({self.x},{self.y})"

    def __repr__(self):
        return f"Pos({self.x},{self.y})"

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def add_dist(self, dist):
        self.dists.append(dist)
cs = []
with open("input_data/ex11_data") as data:
    for row in data:
        cs.append(row.strip())

def empty_col(mat, i):
    return not any([row[i].isdigit() for row in mat])

def insert_col(mat, i):
    for j, r in enumerate(mat):
        mat[j].insert(i, '.')

def get_mat(data):
    ti = time()
    data = [list(row) for row in data]
    k = 1
    for i, r in enumerate(data):
        for j, l in enumerate(r):
            if data[i][j] == "#":
                data[i][j] = str(k)
                k += 1
    print(time() - ti, "get mat done")
    return data
def expand_galax(mat):
    ti = time()
    cmat = copy.deepcopy(mat)
    j = 0
    for i in range(len(cmat)):
        if not any([l.isdigit() for l in cmat[i]]):
            mat.insert(j, mat[j].copy())
            j += 1
        j += 1
    #cmat = copy.deepcopy(mat)
    j = 0
    for i in range(len(cmat[0])):
        if empty_col(cmat, i):
            print(i, "is empty")
            insert_col(mat, j)
            j += 1
        j += 1
    #print(time() - ti, "galaxy expanded")
    return mat

def get_elems(mat):
    eld = dict()
    #ti = time()
    for i, r in enumerate(mat):
        for j, l in enumerate(r):
            if mat[i][j].isdigit():
                eld[l] = Pos(i,j)
    #print(time() - ti, "elems gotten")
    return eld

def get_distances(eld):
    visited = set()
    for key in eld.keys():
        visited.add(key)
        unvis = set(eld.keys()).difference(visited)
        for k2 in unvis:
            eld[key].add_dist(eld[key].dist(eld[k2]))

    return eld

def dist_sum(eld):
    res = 0
    for key in eld:
        res += sum(eld[key].dists)
    return res

sample = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")


galax = get_mat(cs)
print("\n".join([str(row) for row in galax]))
print("-----------------------")
galaxe = expand_galax(galax)
print("\n".join([str(row) for row in galax]))
elems = get_elems(galaxe)
elems = get_distances(elems)
dist = dist_sum(elems)

# print("\n".join([str(row) for row in galax]))
# print(elems)
print(dist)
