# part 1
from heapdict import heapdict
def solve():
    with open("input.txt") as f:
        neighs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inp = [[int(x) for x in s.strip()] for s in f.readlines()]
        h = len(inp)
        l = len(inp[0])
        shortest = [[-1 for _ in range(l)] for _ in range(h)] # grid with shortest paths to each element
        shortest[0][0] = 0
        que = heapdict()
        que[(0, 0)] = 0
        visited = set()
        # standard Didjkstra's algorithm 
        while que:
            node, dist = que.popitem()
            visited.add(node)
            # check neighbours
            for n in neighs:
                neigh = (node[0] + n[0], node[1] + n[1])
                # check they are valid and not in visited
                if (0 <= neigh[0] < l and 0 <= neigh[1] < h and
                    neigh not in visited):
                        new_dist = shortest[node[0]][node[1]] + inp[neigh[0]][neigh[1]]
                        # check if the new distance is shorter than the current one
                        if new_dist < shortest[neigh[0]][neigh[1]] or shortest[neigh[0]][neigh[1]] == -1:
                            shortest[neigh[0]][neigh[1]] = new_dist
                            que[neigh] = new_dist
        print("Shortest path:", shortest[-1][-1])
solve()

# part 2
# pretty much the sane thing as in part 1, except with the grid expanded
from heapdict import heapdict
def solve():
    with open("input.txt") as f:
        neighs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inp = [[int(x) for x in s.strip()] for s in f.readlines()]
        h = len(inp) * 5
        l = len(inp[0]) * 5
        inp = expansion_jutsu(inp, h)
        shortest = [[-1 for _ in range(l)] for _ in range(h)]
        shortest[0][0] = 0
        que = heapdict()
        que[(0, 0)] = 0
        visited = set()
        # standard Didjkstra's algorithm 
        while que:
            node, dist = que.popitem()
            visited.add(node)
            # check neighbours
            for n in neighs:
                neigh = (node[0] + n[0], node[1] + n[1])
                # check they are valid and not in visited
                if (0 <= neigh[0] < l and 0 <= neigh[1] < h and
                    neigh not in visited):
                        new_dist = shortest[node[0]][node[1]] + inp[neigh[0]][neigh[1]]
                        if new_dist < shortest[neigh[0]][neigh[1]] or shortest[neigh[0]][neigh[1]] == -1:
                            shortest[neigh[0]][neigh[1]] = new_dist
                            que[neigh] = new_dist
        print("Shortest path:", shortest[-1][-1])

def expansion_jutsu(grid, h):
    top = []
    for x in grid:
        temp = []
        for i in range(5):
            temp += [(d + i) % 9 if (d+i) != 9 else 9 for d in x]
        top.append(temp[:])
    ret = top.copy()
    for i in range(1, 5):
        for row in top:
            ret.append([(d+i) % 9 if (d+i) != 9 else 9 for d in row])
    return ret
solve()