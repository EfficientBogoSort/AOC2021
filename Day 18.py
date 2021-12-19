import json
import math
# all parts
def solve():
    with open("input.txt") as f:
        first = process_inp(f.readline())
        lines = [first]
        reduce(first)
        max_mag = 0

        # sums all snailnumbers together
        for line in f.readlines():
            first = add_nums(first, line)
            reduce(first)
            lines.append(process_inp(line.strip()))
        print("Sum Magnitude:", count_mag(listify(first)))

        # calculates the max magnitude between any two snailnumbers
        for i in range(len(lines)):
            for j in range(len(lines)):
                if i != j:
                    tgt = ['[']
                    tgt += lines[i]
                    tgt.append(',')
                    tgt += lines[j]
                    tgt.append(']')
                    reduce(tgt)
                    max_mag = max(max_mag, count_mag(listify(tgt)))
        print(max_mag)
def check_explosions(num):
    """
    Check all opening brackets for explosions
    Takes the snailnumber as input in the split string form
    """
    i = 0
    while i < len(num):
        if num[i] == '[':
            if check_explode(num, i):
                explode(num, i)
                return True
        i += 1
    return False

def reduce(num):
    """Reduces a snailnumber in the split string form"""
    while check_explosions(num) or check_split(num):
        continue
def check_explode(num, i):
    """
    Checks if an explosion occurs in the current pair
    Takes as input the snailnumber in the split string form
    and the index of the opening breacket of the pair
    Returns whether there was an explosion
    """
    openers = 0
    closer = 0
    for n in range(i-1, -1, -1):
        if num[n] == '[':
            if closer > 0:
                closer -= 1
            else:
                openers += 1
        elif num[n] == ']':
            closer += 1
        if openers >= 4:
            return True
    return False

def process_inp(inp):
    """
    Converts a snailnumber string form to split string form
    """
    ret = []
    tmp = []
    for i in range(len(inp)):
        if inp[i] in '[],':
            if tmp:
                g = "".join(tmp)
                ret.append(int(g))
                tmp.clear()
            ret.append(inp[i])
        elif inp[i].isdigit():
            tmp.append(inp[i])
    return ret

def explode(num, i):
    """
    Performs an explosion
    Takes as input num, as snailnumber as a list in the split string form,
    and the index of the explosion
    """
    d1 = num[i+1]
    d2 = num[i+3]
    for j in range(i-1, -1, -1):
        if isinstance(num[j], int):
            num[j] += d1
            break
    for j in range(i+4, len(num)):
        if isinstance(num[j], int):
            num[j] += d2
            break
    num[i] = 0
    for _ in range(4):
        num.pop(i+1)

def add_nums(num1, num2):
    """
    Adds two snailnumbers. Input num1 is a snailnumber as a list in the
    split string form, and num2 is a string of the snailnunmber
    """
    ret = ['[']
    ret += num1
    ret.append(',')
    ret += process_inp(num2)
    ret.append(']')

    return ret

def check_split(num):
    """
    Checks for splits and splits if necessary
    Takes a snailnumber as a list in the form of a split string, eg ['[', 1, ',']....
    Outputs a boolean indicating if any splits occurred 
    """
    for j in range(len(num)):
        if isinstance(num[j], int) and num[j] > 9:
            tmp = num[j]
            num[j] = ']'
            num.insert(j, int(math.ceil(tmp/2)))
            num.insert(j, ',')
            num.insert(j, int(math.floor(tmp/2)))
            num.insert(j, '[')
            return True
    return False

def listify(num):
    """
    Converts a snailnumber as a list in the split string form to a
    list with depth
    """
    return json.loads("".join([str(x) for x in num]))

def count_mag(num):
    """
    calculates the maginuted of a number
    Takes a snailnumber as a list with depth, eg [[1, [2,3]], 4],
    as input and outputs the magnitude as an integer
    """
    if not isinstance(num[0], int):
        num[0] = count_mag(num[0])
    if not isinstance(num[1], int):
        num[1] = count_mag(num[1])
    return 3 * num[0] + 2 * num[1]
solve()