from collections import defaultdict as dd
from math import ceil
def solve():
    with open("input.txt") as f:
        inp = list(f.readline().strip())
        rules = {}
        f.readline()
        steps = 40
        counts = dd(int)
        for x in f.readlines():
            x = x.strip().split()
            rules[x[0]] = x[-1]
        curr = dd(int)
        for x in range(1, len(inp)):
            d = str(inp[x-1] + inp[x])
            curr[d] += 1

        for _ in range(steps):
            t = dd(int)
            for key in curr:
                c1 = str(key[0] + rules[key])
                c2 = str(rules[key] + key[1])
                t[c1] += curr[key]
                t[c2] += curr[key]
            curr = t.copy()
        for key in curr:
            counts[key[0]] += curr[key] / 2
            counts[key[1]] += curr[key] / 2
        for key in counts:
            counts[key] = ceil(counts[key])
        print(max(counts.values()) - min(counts.values()))
solve()