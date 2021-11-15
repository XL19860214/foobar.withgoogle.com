# Copyright (c) Xuwei Li

from itertools import permutations


def floyd_warshall_algorithm(matrix):
    dist = matrix
    size = len(matrix)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def solution(times, times_limit):
    size = len(times)
    if size < 3 or size > 7 or times_limit < 0 or times_limit > 999:
        return False

    bunnies_size = size - 2
    dist = floyd_warshall_algorithm(times)

    # Check negative cycle
    if any([dist[i][i] for i in range(size)]):
        return list(range(bunnies_size))
    else:
        for num_bunnies in range(bunnies_size, 0, -1):
            for path in permutations(range(bunnies_size), num_bunnies):
                length = 0
                last_node = 0

                for bunny in path:
                    bunny += 1
                    length += dist[last_node][bunny]
                    last_node = bunny

                length += dist[last_node][size - 1]

                if length <= times_limit:
                    return sorted(path)
        return []


if __name__ == '__main__':
    times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    times_limit = 1
    print('solution({}, {})'.format(times, times_limit))
    print(solution(times, times_limit))

    times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    times_limit = 3
    print('solution({}, {})'.format(times, times_limit))
    print(solution(times, times_limit))
