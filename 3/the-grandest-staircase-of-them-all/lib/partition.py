# Copyright (c) Xuwei Li


def sum(n):
    return len(partitions(n))


def partitions(n):
    p = set()
    p.add((n,))
    for x in range(1, n):
        for y in partitions(n - x):
            p.add(tuple(sorted((x,) + y)))
    return p
