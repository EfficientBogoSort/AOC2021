def solve():
    with open("input.txt") as f:
        last_score = -1
        inp = [int(x) for x in f.readline().split(",")]
        nums = set()
        for x in inp:
            nums.add(x)
        drawn = set()
        bingoed = set()
        f.readline()
        boards = read_boards(f)
        counts = []

        # counter for all boards
        for x in range(len(boards)):
            counts.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        for num in inp:
            drawn.add(num)

            # mark the number for each board
            for i in range(len(boards)):
                if num in boards[i]:
                    counts[i][0][boards[i][num][0]] += 1
                    counts[i][1][boards[i][num][1]] += 1

            # part 1
            """
            if (c := bingo(counts, bingoed)) != -1:
                total = 0
                for key in boards[c]:
                    if  key not in drawn:
                        total += key
                print(total * num)
            """
            # part 2
            """
            while (c := bingo(counts, bingoed)) != -1:
                bingoed.add(c)
                total = 0
                for key in boards[c]:
                    if key not in drawn:
                        total += key
                last_score = total * num
        
            """
        # part of part 2
        # print(last_score)

def read_boards(inp):
    ret = []
    tmp = {}
    row = 0
    for line in inp:
        if line != '\n':
            nums = [int(i) for i in line.split(" ") if i != '']
            for i in range(5):
                tmp[nums[i]] = (row, i)
            row += 1
        else:
            ret.append(tmp)
            tmp = {}
            row = 0
    ret.append(tmp)
    return ret

def bingo(counts, bingoed):
    for board in range(len(counts)):
        if board not in bingoed:
            for i in range(5):
                if counts[board][0][i] == 5 or counts[board][1][i] == 5:
                    return board
    return -1

solve()
