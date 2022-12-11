def solve():
    with open("input.txt") as f:
        board = []
        xmax = -1
        ymax = -1
        hor = []
        vert = []
        diags = []

        for line in f:
            line = line.replace(',', "->")
            tmp = [int(i) for i in line.split("->")]
            xmax = max([tmp[0], tmp[2], xmax])
            ymax = max([tmp[1], tmp[3], ymax])
            if tmp[0] == tmp[2]:
                vert.append((tmp[2], tmp[1], tmp[3]))
            elif tmp[1] == tmp[3]:
                hor.append((tmp[1], tmp[0], tmp[2]))
            else:
                info = []
                if tmp[0] > tmp[2]:
                    info.append(-1)
                else:
                    info.append(1)
                if tmp[1] > tmp[3]:
                    info.append(-1)
                else:
                    info.append(1)
                diags.append(info + tmp)
        for i in range(ymax + 1):
            board.append([0 for x in range(xmax + 1)])

        for i in range(len(hor)):
            for j in range(min(hor[i][1], hor[i][2]), max(hor[i][1], hor[i][2]) + 1):
                board[hor[i][0]][j] += 1
        for i in range(len(vert)):
            for j in range(min(vert[i][1], vert[i][2]), max(vert[i][1], vert[i][2]) + 1):
                board[j][vert[i][0]] += 1
        for i in range(len(diags)):
            x1 = diags[i][2]
            x2 = diags[i][4]
            y1 = diags[i][3]
            y2 = diags[i][-1]
            while x1 != x2 and y1 != y2:
                board[y1][x1] += 1
                x1 += diags[i][0]
                y1 += diags[i][1]
            board[y1][x1] += 1
        tot = 0
        for x in board:
            for y in x:
                if y > 1:
                    tot += 1
        print(tot)
solve()
