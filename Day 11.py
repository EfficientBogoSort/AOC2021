def solve():
    with open("input.txt") as f:
        inp = [[int(c) for c in x.strip()] for x in f.readlines()]
        n_steps = 1000
        tot = 0
        flashed = set()
        for x in range(n_steps):
            flashed.clear()
            inp = [[x+1 for x in c] for c in inp]
            flashes = 1
            while flashes > 0:
                flashes = 0
                # check if any octopus flashed, and increase surrounding energy
                # by 1 if so
                for y in range(len(inp)):
                    for v in range(len(inp[0])):
                        if inp[y][v] > 9:
                            infect(inp, v, y, flashed)
                            flashes += 1
                            inp[y][v] = 0
                            flashed.add((v, y))
                tot += flashes
                if all_flashed(inp):
                    print("First time all flashed:", x)
        print("Total flashes:", tot)

def infect(grid, x, y, flashed):

    # check for all octopi around the current octopus and increase their
    # energy if they haven't been increased in the current step
    if x > 0:
        # top left
        if y > 0 and (x-1, y-1) not in flashed:
            grid[y-1][x-1] += 1
        if (x - 1, y) not in flashed:
            grid[y][x-1] += 1
        if y < len(grid) - 1 and (x-1, y+1) not in flashed:
            grid[y+1][x-1] += 1

    if y > 0 and (x, y - 1) not in flashed:
        grid[y-1][x] += 1
    if y < len(grid) - 1 and (x, y + 1) not in flashed:
        grid[y+1][x] += 1
    if x < len(grid[0]) - 1:
        if y > 0 and (x + 1, y - 1) not in flashed:
            grid[y-1][x+1] += 1
        if (x + 1, y) not in flashed:
            grid[y][x+1] += 1
        if y < len(grid) - 1 and (x + 1, y + 1) not in flashed:
            grid[y+1][x+1] += 1
def all_flashed(grid):
    # all octopi flash when all their energy is 0
    for x in grid:
        for y in x:
            if y != 0:
                return False
    return True
solve()