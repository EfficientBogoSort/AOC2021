def solve():
    with open("input.txt") as f:
        max_x = -1
        max_y = -1
        points = set()
        counted = -1
        # get the max x and y to get the size of the grid
        for x in f:
            if x == '\n':
                break
            x = x.strip().split(",")
            points.add((int(x[0]), int(x[1])))
        # process all folds
        for x in f.readlines():
            lin = x.strip().split(" ")[2].split("=")
            points = fold(lin[0], int(lin[1]), points)
            # only count the number of # after the first fold
            if counted == -1:
                counted = len(points)
        for point in points:
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        fill_grid(grid, points)
        print("Number of points after first fold:", counted)
        for x in grid:
            print(x)
            
            
def fill_grid(grid, points):
    # fill all the filled spots
    for point in points:
        grid[point[1]][point[0]] = '#'


def fold(axis, n, points):
    ret = points.copy()
    if axis == "x":
        for point in points:
            if point[0] > n:
                c = 2 * n - point[0]
                if c > -1:
                    ret.add((2 * n - point[0], point[1]))
                ret.remove(point)
        return ret
    else:
        for point in points:
            if point[1] > n:
                c = 2 * n - point[1]
                if c > -1:
                    ret.add((point[0], 2 * n - point[1]))
                ret.remove(point)
        return ret
    
    
solve()