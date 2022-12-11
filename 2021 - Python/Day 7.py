import math

def solve():
    with open("example.txt") as f:
        nums = [int(x) for x in f.readline().split(",")]
        a = max(nums)
        b = min(nums)
        print(nums)
        minFuel = -1
        for i in range(b, a+1):
            k = 0
            for n in nums:
                # part 1
                """
                k += math.fabs(i-n)
                """
                # part 2
                """
                dist = math.fabs(i-n)
                k += dist * (dist+1)/2
                """
            if minFuel == -1 or k < minFuel:
                minFuel = k
        print(minFuel)
solve()
