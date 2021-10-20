# Copyright (c) Xuwei Li


import math


def solution(h, q):
    if min(q) < 1:
        return False
    if math.log(max(q), 2) > h:
        return False
    apex = 2 ** h - 1
    return [getParentNode(apex, node) for node in q]


def getParentNode(apex, target):
    if apex == target:
        return -1

    current_node = apex
    diff = apex

    while diff > 1:
        parent = current_node
        # Move down one level
        diff = diff >> 1
        # Locate two children
        left_child = current_node - diff - 1
        right_child = current_node - 1
        # Check if target is one of children
        if target == left_child or target == right_child:
            return parent
        # Assign current node for next loop
        if target < left_child:
            current_node = left_child
        elif target > left_child:
            current_node = right_child

    return False
