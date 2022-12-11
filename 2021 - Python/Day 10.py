from queue import LifoQueue
comp = {'(': ')', '[' : ']', '{':'}', '<' : '>'}

def solve():
    with open("input.txt") as f:
        stack = LifoQueue()
        openings = {'(', '[', '{', '<'}
        errors = []
        vals = {')': 3, ']': 57, '}': 1197, '>': 25137}

        scores = []
        for line in f.readlines():
            for c in list(line):
                if c == '\n':
                    break
                if c in openings:
                    stack.put(c)
                else:
                    if c != comp[stack.get()]:
                        errors.append(c)
                        stack = LifoQueue()
                        break
            if stack.qsize() != 0:
                scores.append(get_score(stack))
            stack = LifoQueue()
        tot = sum([vals[error] for error in errors])

        print("part 1:", tot)
        print("part 2:", sorted(scores)[int((len(scores) - 1) / 2)])
def get_score(stack):
    vals = {')': 1, ']': 2, '}': 3, '>': 4}
    tot = 0
    while stack.qsize() != 0:
        tot *= 5
        tot += vals[comp[stack.get()]]
    return tot
