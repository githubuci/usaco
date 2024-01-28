# Problem 2
# 5
# 5
# 1 2 2 2 3
# 6
# 1 2 3 1 2 3
# 6
# 1 1 1 2 2 2
# 3
# 3 2 3
# 2
# 2 1

from collections import defaultdict


def get_hays(arr):
    indexes = defaultdict(int)
    distances = defaultdict(int)

    for index, a in enumerate(arr):
        if a in indexes:
            distance = index - indexes[a]
            distances[a] = min(distances[a], distance) if distances[a] else distance
        indexes[a] = index

    # keep this in the appearance order?
    results = [k for k, v in distances.items() if v < 3]
    if not results:
        return -1

    return results


with open('/Users/garyluo/workspace1/scio/experimental/users/garyluo/problem2.txt') as f:
    t = int(f.readline())
    for i in range(t):
        n = int(f.readline())
        hays = [int(j) for j in f.readline().split()]
        print(get_hays(hays))
