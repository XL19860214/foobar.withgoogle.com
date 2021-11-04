# Copyright (c) Xuwei Li

from itertools import combinations


def solution(num_buns, num_required):
    if num_buns < 1 or num_buns > 9 or num_required < 0 or num_required > 9:
        return False
    if num_buns < num_required:
        return False

    key_chains = [[] for i in range(num_buns)]
    keys_per_lock = num_buns - (num_required - 1)
    for lock_key, bunnies in enumerate(combinations(range(num_buns), keys_per_lock)):
        for bunny in bunnies:
            key_chains[bunny].append(lock_key)

    return key_chains
