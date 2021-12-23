def solve():
    with open("input.txt") as f:
        pos = [int(x[-1]) for x in f.read().split("\n")]
        sc = [0, 0]
        p = i = 0
        summing_score = 6
        j = 1
        while sc[0] < 1000 and sc[1] < 1000:
            if (c := (pos[p] + summing_score) % 10) == 0:
                pos[p] = 10
            else:
                pos[p] = c
            sc[p] += pos[p]
            p += j
            j *= -1
            summing_score += 9
            i += 3
        print(sc, i)

solve()


# part 2
# not my code
# code taken from
# https://www.youtube.com/watch?v=a6ZdJEntKkk&t=731s
gg = {}
def solve():
    with open("input.txt") as f:
        pos = [int(x[-1]) for x in f.read().split("\n")]
        print(max(count_win(pos[0] - 1, 0, pos[1] - 1, 0)))



def count_win(pos1, sc1, pos2,sc2):
    if sc1 >= 21:
        return 1,0
    if sc2 >= 21:
        return 0,1
    if (pos1, sc1, pos2, sc2) in gg:
        return gg[(pos1, sc1, pos2, sc2)]
    ret = (0,0)
    for i in [1,2,3]:
        for j in [1,2,3]:
            for k in [1,2,3]:
                new_pos1 = (pos1 + i + j + k) % 10
                new_sc1 = sc1 + new_pos1 + 1
                a, b = count_win(pos2, sc2, new_pos1, new_sc1)
                ret = (ret[0] + b, ret[1] + a)
    gg[(pos1, sc1, pos2,sc2)] = ret
    return ret
solve()


