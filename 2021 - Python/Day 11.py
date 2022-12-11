def solve():
    with open("input.txt") as f:
        inp = [[int(c) for c in x.strip()] for x in f.readlines()]
        n_steps = 1000
        tot = 0
        flashed = set()
        first_flash = -1
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
                if all_flashed(inp) and first_flash == -1:
                    print("First time all flashed:", x)
                    first_flash = x
        print("Total flashes:", tot)

def infect(grid, x, y, flashed):
    # check for all octopi around the current octopus and increase their
    # energy if they haven't been increased in the current step
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (j != 0 or i != 0) and (x + j, y + i) not in flashed \
                    and 0 <= x + j < len(grid[0]) and 0 <= y + i < len(grid):
                grid[y+i][x+j] += 1


def all_flashed(grid):
    # all octopi flash when all their energy is 0
    for x in grid:
        for y in x:
            if y != 0:
                return False
    return True
solve()
