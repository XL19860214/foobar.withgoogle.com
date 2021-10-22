# Copyright (c) Xuwei Li


def solution(map):
    path = findPath(map, True)
    if path:
        return len(path)
    
    paths = {}
    for y, row in enumerate(map):
        for x in row:
            if map[y][x] == 1:
                newMap = map.copy()
                newMap[y][x] = 0
                path = findPath(newMap)
                if path:
                    paths[len(path)] = path
    # print(paths) #DEBUG

    return min(paths)


def findPath(map, optimize = False):
    history = []
    blacklist = []
    w = len(map[0])
    h = len(map)
    # print('w', w, 'h', h) #DEBUG
    x = 0
    y = 0
    history.append((x, y))
    while history[len(history) - 1][0] != w - 1 or history[len(history) - 1][1] != h - 1:
        if x + 1 < w and map[y][x + 1] == 0 and (x + 1, y) not in blacklist and (x + 1, y) not in history:
            x += 1
        elif y + 1 < h and map[y + 1][x] == 0 and (x, y + 1) not in blacklist and (x, y + 1) not in history:
            y += 1
        elif x - 1 >= 0 and map[y][x - 1] == 0 and (x - 1, y) not in blacklist and (x - 1, y) not in history:
            x -= 1
        elif y - 1 >= 0 and map[y - 1][x] == 0 and (x, y - 1) not in blacklist and (x, y - 1) not in history:
            y -= 1
        else: # Fallback
            last = history.pop()
            blacklist.append(last)
            # print('Blacklist', last) #DEBUG
            if last == (0, 0):
                # print('Must break wall.') #DEBUG
                return False
            fallback = history.pop()
            x = fallback[0]
            y = fallback[1]

        history.append((x, y))
        # print('Move to', (x, y)) #DEBUG
    
    # print(history) #DEBUG

    if optimize:
        #
        walls = {}
        for i, pos in enumerate(history):
            x_ = pos[0]
            y_ = pos[1]
            for j in range(0, i)[::-1]:
                # print(pos, j, (history[j])) #DEBUG
                if (history[j][0] + 2, history[j][1]) == (x_, y_):
                    if map[y_][x_ - 1] == 1:
                        wall = (x_ - 1, y_)
                        walls[(j, i)] = wall
                elif (history[j][0], history[j][1] + 2) == (x_, y_):
                    if map[y_ - 1][x_] == 1:
                        wall = (x_, y_ - 1)
                        walls[(j, i)] = wall
                elif (history[j][0] - 2, history[j][1]) == (x_, y_):
                    if map[y_][x_ + 1] == 1:
                        wall = (x_ + 1, y_)
                        walls[(j, i)] = wall
                elif (history[j][0], history[j][1] - 2) == (x_, y_):
                    if map[y_ + 1][x_] == 1:
                        wall = (x_, y_ + 1)
                        walls[(j, i)] = wall
        
        longest = None
        for range_ in walls.keys():
            if longest == None or range_[1] - range_[0] > longest[1] - longest[0]:
                longest = range_
            
        if walls:
            # print('walls', walls) #DEBUG
            history[longest[0]:longest[1]] = walls[longest]

        # print(history) #DEBUG

    return history
