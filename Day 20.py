import copy
def solve():
    with open("input.txt") as f:
        algo, img = f.read().split("\n\n")
        enhancement_num = 2
        img = img.split("\n")
        out_img = add_input_img(img, enhancement_num)
        for x in range(enhancement_num):
            out_img = enhance(out_img, algo)
            alternate(out_img, algo, x)
        ret = 0
        for y in out_img:
            for x in y:
               if x == '#':
                   ret += 1
        print(ret)

def add_input_img(img, n):
    out_img = [['.' for _ in range(len(img[0]) + 4*n)] for _ in range(len(img) + 4*n)]
    for i in range(len(img)):
        for j in range(len(img[0])):
            out_img[i + 2*n][j + 2*n] = img[i][j]
    return out_img

def enhance(img, algo):
    ret = copy.deepcopy(img)
    for i in range(1, len(img) - 1):
        for j in range(1, len(img[0]) - 1):
            ret[i][j] = transform(img, j, i, algo)
    return ret


def transform(img, x, y, algo):
    ret = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if img[y+i][x+j] == '.':
                ret.append('0')
            else:
                ret.append('1')
    return algo[int("".join(ret), 2)]

def alternate(img, algo, n):
    s = ''
    if n % 2 == 0:
        s = algo[0]
    else:
        s = algo[511]
    for x in range(len(img)):
        img[x][0] = s
        img[x][-1] = s
    for x in range(len(img[0])):
        img[0][x] = s
        img[-1][x] = s
solve()



