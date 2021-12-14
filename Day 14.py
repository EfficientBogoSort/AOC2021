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
        # get the initial frequence of polymers
        for x in range(1, len(inp)):
            d = str(inp[x-1] + inp[x])
            curr[d] += 1
        # perform all the steps. 
        for _ in range(steps):
            t = dd(int)
            for key in curr:
                # Each element will become two elements, so AB -> C would be: AC, CB
                # The frequency of AC and CB will be the same as the parent
                c1 = str(key[0] + rules[key])
                c2 = str(rules[key] + key[1])
                t[c1] += curr[key]
                t[c2] += curr[key]
            curr = t.copy()
        # add up half of the counts for each element since they appear twice (once as the start and once as the end)
        for key in curr:
            counts[key[0]] += curr[key] / 2
            counts[key[1]] += curr[key] / 2
        # round up any counts
        for key in counts:
            counts[key] = ceil(counts[key])
        print(max(counts.values()) - min(counts.values()))
solve()