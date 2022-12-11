from collections import defaultdict

n = 0
def solve():
    with open("input.txt") as f:
        paths = defaultdict()
        visited = set()
        # create an adjacency list
        for x in f.readlines():
            x = x.strip().split("-")
            try:
                paths[x[0]].add(x[1])
            except KeyError:
                paths[x[0]] = {x[1]}
            try:
                paths[x[1]].add(x[0])
            except KeyError:
                paths[x[1]] = {x[0]}
        dfs(paths, 'start', 'end', visited)
        print("Number of paths:", n)


def dfs(paths, curr, end, visited):
    global n
    # only mark small caves as visited
    if curr.islower():
        visited.add(curr)
    for neigh in paths[curr]:
        if neigh == end:
            n += 1
        elif neigh not in visited:
            dfs(paths, neigh, end, visited.copy())
solve()

# part 2
def solve2():
    with open("input.txt") as f:
        paths = defaultdict()
        visited = set()
        small_caves = set()
        all_paths = []
        count = 0
        for x in f.readlines():
            x = x.strip().split("-")
            try:
                paths[x[0]].add(x[1])
            except KeyError:
                paths[x[0]] = {x[1]}
            try:
                paths[x[1]].add(x[0])
            except KeyError:
                paths[x[1]] = {x[0]}
            if x[0].islower() and x[0] != 'start' and x[0] != 'end':
                small_caves.add(x[0])
            if x[1].islower() and x[1] != 'start' and x[1] != 'end':
                small_caves.add(x[1])
        # check for every small cave being able to be visited twice
        for h in small_caves:
            count += 1
            print(count, "/ ", len(small_caves))
            dfs(paths, 'start', 'end', visited, h, False, [], all_paths)
        print("Number of paths:", n)
        print(len(all_paths))


def dfs(paths, curr, end, visited, small, first_visit, v, all_paths):
    global n
    # only add the selected cave in the second visit
    if (curr.islower() and curr != small) or (curr == small and first_visit):
        visited.add(curr)
    if curr == small and not first_visit:
        first_visit = True
    for neigh in paths[curr]:
        if neigh == end:
            n += 1
            b = v + [curr]
            # some paths will be repeated, so only add if it's not already in it
            # there might be a fix for it, but it's 3 am and I can't be bothered
            if b not in all_paths:
                all_paths.append(b)
        elif neigh not in visited:
            dfs(paths, neigh, end, visited.copy(), small, first_visit, v + [curr], all_paths)
solve()


