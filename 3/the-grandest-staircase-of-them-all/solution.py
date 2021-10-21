# Copyright (c) Xuwei Li


def solution(n):
    if n < 3 or n > 200:
        return False

    m = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            m[j] += m[j - i]

    return m[n] - 1
