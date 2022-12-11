# part 1
def solve():
    with open("input.txt") as f:
        set_on = set()
        for inst in f.readlines():
            inst = inst.strip().split(" ")
            follow = True
            limits = []
            for coord in inst[1].split(","):
                if int((c := coord[2:].split(".."))[0]) < -50 or int(c[1]) > 50:
                    follow = False
                    break
                limits.append(int(c[0]))
                limits.append((int(c[1])))
            if follow:
                for i in range(limits[0], limits[1] + 1):
                    for j in range(limits[2], limits[3] + 1):
                        for k in range(limits[4], limits[5] + 1):
                            if inst[0] == 'on':
                                set_on.add((i,j,k))
                            else:
                                if (i,j,k) in set_on:
                                    set_on.remove((i,j,k))
        print(len(set_on))
