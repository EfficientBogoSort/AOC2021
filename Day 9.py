
# part1
def solve1():
    with open("input.txt") as f:
        ret = 0
        nums = []
        visited = set()
        for x in f.readlines():
            g = []
            for i in x:
                if i.isdigit():
                    g.append(int(i))
            nums.append(g)
        for y in range(len(nums)):
            for x in range(len(nums[0])):
                if check_adj(nums, x, y):
                    ret += 1 + nums[y][x]
        print(ret)
def check_adj(nums, x, y):
    n = nums[y][x]
    if x > 0:
        if n >= nums[y][x-1]:
            return False
    if x < len(nums[0]) - 1:
        if n >= nums[y][x+1]:
            return False
    if y > 0:
        if n >= nums[y-1][x]:
            return False
    if y < len(nums) - 1:
        if n >= nums[y+1][x]:
            return False
    return True

# part 2
def solve():
    with open("input.txt") as f:
        ret = 0
        nums = []
        visited = set()
        low_points = []
        sizes = []
        a = b = c = 0
        for x in f.readlines():
            g = []
            for i in x:
                if i.isdigit():
                    g.append(int(i))
            nums.append(g)
        for y in range(len(nums)):
            for x in range(len(nums[0])):
                if check_adj(nums, x, y):
                    g = (y, x)
                    low_points.append(g)

        convert_map(nums)
        for point in low_points:
            sizes.append(do_bfs(nums, point, visited))
            print()
        sizes = sorted(sizes, reverse=True)
        print(sizes[0] * sizes[1] * sizes[2])

def check_adj(nums, x, y):
    n = nums[y][x]
    if x > 0:
        if n >= nums[y][x-1]:
            return False
    if x < len(nums[0]) - 1:
        if n >= nums[y][x+1]:
            return False
    if y > 0:
        if n >= nums[y-1][x]:
            return False
    if y < len(nums) - 1:
        if n >= nums[y+1][x]:
            return False
    return True


def convert_map(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == 9:
                nums[i][j] = 0
            else:
                nums[i][j] = 1

def do_bfs(nums, start, visited):
    if nums[start[0]][start[1]] == 0 or start in visited:
        visited.add(start)
        return 0
    tot = 0
    visited.add(start)
    if start[0] > 0 and (start[0] - 1, start[1]) not in visited:
        tot += do_bfs(nums, (start[0] - 1, start[1]), visited)
    if start[0] < len(nums) - 1 and (start[0] + 1, start[1]) not in visited:
        tot += do_bfs(nums, (start[0] + 1, start[1]), visited)
    if start[1] > 0 and (start[0], start[1] - 1) not in visited:
        tot += do_bfs(nums, (start[0], start[1] - 1), visited)
    if start[1] < len(nums[0]) - 1 and (start[0], start[1] + 1) not in visited:
        tot += do_bfs(nums, (start[0], start[1] + 1), visited)

    return 1 + tot