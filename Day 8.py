
# part 1
def solve():
    with open("input.txt") as f:
        inp = f.readline().split("|")
        code = [x for x in inp[1].split(" ") if len(x) != 0]
        count = 0
        for x in code:
            t = len(x)
            if t == 2 or t == 3 or t == 4 or t == 7:
                count += 1
        print(count) 


# part 2
"""
def solve():
    with open("input.txt") as f:
        count = 0
        for i in f.readlines():
            numDict = {}
            group1 = []
            group2 = []
            one = ""
            four =""
            inp = i.split("|")
            nums = [x for x in inp[0].split(" ") if len(x) != 0]
            code = [x for x in inp[1].split(" ") if len(x) != 0]

            # identify unique numbers
            for x in nums:
                x = x.replace('\n', "")
                x = "".join(sorted(x))
                l = len(x)
                if l  == 5:
                    group1.append(x)
                elif l  == 6:
                    group2.append(x)
                elif l == 2:
                    numDict[x] = '1'
                    one = x
                elif l == 4:
                    numDict[x] = '4'
                    four = x
                elif l == 3:
                    numDict[x] = '7'
                elif l == 7:
                    numDict[x] = '8'

            # identify all other numbers by pattern
            # add 3, 5, 2 to dict
            find_g1(group1, one, four, numDict)

            # add 6, 9, 0
            find_g2(group2, one, four, numDict)
            g = []
            for x in code:
                x = x.replace("\n", "")
                x = "".join(sorted(x))
                g.append(numDict[x])
            count += int("".join(g))
        print(count)

def find_g1(nums, one, four, numDict):
    ret = []
    checked = set()
    one = set(one)
    # find 3
    for i in range(len(nums)):
        t = set(nums[i])
        if one.issubset(t):
            ret.append(nums[i])
            checked.add(i)
            break
    # find 5
    four = set(four)
    for i in range(len(nums)):
        t = set(nums[i])
        if i not in checked and len(t.intersection(four)) == 3:
            ret.append(nums[i])
            checked.add(i)
    for i in range(len(nums)):
        if i not in checked:
            ret.append(nums[i])
    numDict[ret[0]] = '3'
    numDict[ret[1]] = '5'
    numDict[ret[2]] = '2'

def find_g2(nums, one, four, numDict):
    ret = []
    checked = set()
    one = set(one)
    # find 6
    for i in range(len(nums)):
        t = set(nums[i])
        if not one.issubset(nums[i]):
            ret.append(nums[i])
            checked.add(i)

            break
    # find 9
    four = set(four)
    for i in range(len(nums)):
        if i not in checked:
            t = set(nums[i])
            if four.issubset(nums[i]):
                ret.append(nums[i])
                checked.add(i)
                break
    # find 0
    for i in range(len(nums)):
        if i not in checked:
            ret.append(nums[i])
            break
    # 6, 9, 0
    numDict[ret[0]] = '6'
    numDict[ret[1]] = '9'
    numDict[ret[2]] = '0'
solve()
"""