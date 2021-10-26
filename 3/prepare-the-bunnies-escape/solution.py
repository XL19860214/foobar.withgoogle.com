# Copyright (c) Xuwei Li


def solution(map):
    h = len(map)
    w = len(map[0])
    map1 = distantMap(map, (0, 0))
    map2 = distantMap(map, (w - 1, h - 1))
    # print(map)  #DEBUG
    # print(map1) #DEBUG
    # print(map2) #DEBUG

    p = w * h
    for x in range(w):
        for y in range(h):
            if map1[y][x] and map2[y][x]:
                p = min(map1[y][x] + map2[y][x] - 1, p)

    if p == w * h:
        return False
    return p


def distantMap(map, coordinate):
    h = len(map)
    w = len(map[0])

    # m = [[None] * w] * h
    m = [[None for i in range(w)] for i in range(h)]
    x, y = coordinate
    m[y][x] = 1

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = [coordinate]
    while len(queue) > 0:
        posX, posY = queue.pop(0)
        for move in moves:
            toX, toY = posX + move[0], posY + move[1]
            # print('from', pos, 'to', (toX, toY)) #DEBUG
            if 0 <= toX < w and 0 <= toY < h:
                if m[toY][toX] is None:
                    m[toY][toX] = m[posY][posX] + 1
                    # Disrupt at a wall
                    if map[toY][toX] == 1:
                        continue
                    queue.append((toX, toY))
                    # print((toX, toY)) #DEBUG

    return m
