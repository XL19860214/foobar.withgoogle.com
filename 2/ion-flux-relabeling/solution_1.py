# Copyright (c) Xuwei Li


import math


def solution(h, q):
    # Domain check
    if h < 1 or h > 30:
        return False
    lenQ = len(q)
    if lenQ < 1 or lenQ > 10000:
        return False
    if min(q) < 1:
        return False
    if math.log(max(q), 2) > h:
        return False
    # Optimization
    treeH = min([h, math.ceil(math.log(max(q), 2)) + 1])
    # Process
    tree = Tree(treeH)
    p = []
    for qI in q:
        p.append(tree.nodes[qI].parent)
    return p


class Tree:
    h = None
    apex = None
    nodes = {}
    
    # Construct tree with all nodes
    def __init__(self, h):
        self.h = h
        self.apex = pow(2, h) - 1
        self.addNode(Node(self.apex, 1))
        self.addChain(self.apex, 1)

    # Add chain of nodes
    def addChain(self, start, ceil):
        count = 1
        level = ceil + 1
        parentLabel = start
        while level <= self.h:
            label = start - count
            floor = self.h - level + 1
            siblingFactor = pow(2, floor) - 1
            siblingLabel = label - siblingFactor
            self.addNode(Node(label, level, right=True, parent=parentLabel, sibling=siblingLabel))
            # next loop
            count += 1
            level += 1
            parentLabel = label

    # Add node and sibling node
    def addNode(self, node):
        if node.label not in self.nodes:
            self.nodes[node.label] = node
        # Propagate
        if node.sibling and node.sibling not in self.nodes:
            self.addNode(Node(node.sibling, node.ceil, parent=node.parent, sibling=node.label))
            self.addChain(node.sibling, node.ceil)


class Node:
    label = None
    right = False
    parent = -1
    sibling = None
    ceil = None

    def __init__(self, label, ceil, right=False, parent=-1, sibling=None):
        self.label = label
        self.ceil = ceil
        # Optional
        self.right = right
        self.parent = parent
        self.sibling = sibling