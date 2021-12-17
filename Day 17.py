def solve():
    with open("input.txt") as f:
        inp = f.readline().strip().split(" ")
        x1 = int(inp[2][2:5])
        x2 = int(inp[2][7:10])
        y1 = int(inp[3][2:5])
        y2 = int(inp[3][7:10])
        maxh = max_height(min(y1, y2))
        print("Max height is:", maxh)
        maxy = max(abs(y1), abs(y2))
        positions = 0
        for x in range(abs(x2) + 1):
            for y in range(-maxy - 1, maxy+1):
                land = land_in_area([x, y], x1, x2, y1, y2)
                if land:
                    positions += 1
        print("Number of different positions that land:", positions)


def land_in_area(vel, x1, x2,y1, y2):
    pos = [0, 0]
    miny = min(y1, y2)
    maxy = max(y1, y2)
    maxh = 0
    while True:
        maxh = max(maxh, pos[1])
        if pos[0] > x2 or (vel[1] < 0 and pos[1] < miny):
            return False
        if x1 <= pos[0] <= x2 and miny <= pos[1] <= maxy:
            return True
        pos[0] += vel[0]
        pos[1] += vel[1]
        if vel[0] != 0:
            c = pos[0] / abs(pos[0])
        else:
            c = 0
        vel[0] -= c
        vel[1] -= 1
        
        
def max_height(miny):
    return miny * (miny+1) / 2
solve()