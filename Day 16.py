import math
def solve():
    with open("input.txt") as f:
        # hex to bin
        htb = {'0': '0000', '1' : '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101'
               , '6': '0110', '7': '0111', '8':'1000', '9': '1001', 'A': '1010',
               'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
        m = f.readline()
        g = []
        for x in m:
            g.append(htb[x])
        g = "".join(g)
        v = []
        n = get_package(g, 0, v)
        print(n[1])
        print(sum(v))
def get_package(nums, n, versions):
    # keep track of all the versions
    versions.append(convert_dec(nums[n:n+3]))
    typ = nums[n+3:n+6]
    b = nums[n+6]
    
    # packet is a literal
    if convert_dec(typ) == 4:
        ret = []
        j = n+6
        while nums[j] == '1':
            ret.append(nums[j + 1:j + 5])
            j += 5
        ret.append(nums[j+1:j+5])
        # converts literal from binary to decimal
        ret = convert_dec("".join(ret))
        j += 5
        return j, ret
    else:
        vals = []
        if b == '0':
            # index of the first subpack
            pack_start = n + 22
            pack_len = convert_dec(nums[n + 7:n + 22])
            pack_end = pack_start + pack_len
            # proces each subpack
            while pack_start < pack_end:
                pack_start, s = get_package(nums, pack_start, versions)
                vals.append(s)
            return pack_start, operation(vals, typ)
        else:
            n_packs = convert_dec(nums[n+7:n+18])
            # index of the first subpack
            pack_start = n + 18

            # proces each subpack
            for _ in range(n_packs):
                pack_start, s = get_package(nums, pack_start, versions)
                vals.append(s)
            return pack_start, operation(vals, typ)
def convert_dec(binary):
    return int(binary, 2)

def operation(vals, operand):
    if operand == '000':
        return sum(vals)
    if operand == '001':
        return math.prod(vals)
    if operand == '010':
        return min(vals)
    if operand == '011':
        return max(vals)
    if operand == '101':
        if len(vals) != 2:
            print("More than 2 values in operation ID 5")
        return 1 if vals[0] > vals[1] else 0
    if operand == '110':
        if len(vals) != 2:
            print("More than 2 values in operation ID 6")
        return 1 if vals[0] < vals[1] else 0
    if operand == '111':
        return 1 if vals[0] == vals[1] else  0
solve()