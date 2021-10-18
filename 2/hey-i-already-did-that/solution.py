# Copyright (c) Xuwei Li

def solution(n, b):
    logs = list()
    id = nextId(n, b)
    logs.append(id['z'])
    # Loop
    next = nextId(id['z'], b)
    while next['z'] not in logs:
        logs.append(next['z'])
        next = nextId(next['z'], b)
    return len(logs) - logs.index(next['z'])


# Calculate next Id
def nextId(n, b):
    # n
    nStr = str(n)
    # x
    xStrList = list(nStr)
    xStrList.sort(reverse=True)
    xStr = ''.join(xStrList)
    # y
    yStrList = list(nStr)
    yStrList.sort()
    yStr = ''.join(yStrList)
    # z
    z = int(xStr, b) - int(yStr, b)
    return { 'n': nStr, 'x': xStr, 'y': yStr, 'z': based(z, b) }


# Convert to based number
def based(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.insert(0, str(n % b))
        n //= b
    return ''.join(digits)
