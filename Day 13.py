def solve():
    with open("input.txt") as f:
        max_x = -1
        max_y = -1
        points = []
        counted = -1
        # get the max x and y to get the size of the grid
        for x in f:
            if x == '\n':
                break
            x = x.strip().split(",")
            points.append((int(x[0]), int(x[1])))
            max_x = max(max_x, int(x[0]))
            max_y = max(max_y, int(x[1]))
        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        fill_grid(grid, points)
        # process all folds
        for x in f.readlines():
            lin = x.strip().split(" ")[2].split("=")
            grid = fold(grid, lin[0], int(lin[1]))
            # only count the number of # after the first fold
            if counted == -1:
                counted = count_n(grid)
        print(counted)
        for x in grid:
            print(x)
def fill_grid(grid, points):
    # fill all the filled spots
    for point in points:
        grid[point[1]][point[0]] = '#'

def fold(grid, axis, n):
    if axis == "x":

        l = len(grid[0])
        for y in range(len(grid)):
            for x in range(n + 1, l):
                c = 2 * n - x
                if grid[y][x] == '#' and c > - 1:
                    grid[y][c] = '#'
        ret = []
        # I am not sure if there's a better way to do this,
        # but the way I figured to resize the width is to manually resize it
        for x in grid:
            ret.append(x[0:n])
        return ret
    else:
        h = len(grid)
        for y in range(n + 1, h):
            for x in range(len(grid[0])):
                c = 2 * n - y
                if grid[y][x] == '#' and c > -1:
                    grid[c][x] = '#'
        return grid[0: n]
def count_n(grid):
    ret = 0
    for y in grid:
        for x in y:
            if x == '#':
                ret += 1
    return ret
solve()