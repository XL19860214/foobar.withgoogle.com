# Copyright (c) Xuwei Li


def solution(n):
    if len(n) > 309:
        return False

    m = int(n)
    
    i = 0
    while m != 1:
        if m == 3:
            m -= 2
            i += 2
            continue
        if m % 2 == 1:
            if (m >> 1) % 2 == 0:
                m -= 1
                i += 1
            else:
                m += 1
                i += 1
        m = m >> 1
        i += 1
        
    return i
