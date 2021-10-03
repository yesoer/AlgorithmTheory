from ..utils import *


test_weighted_edges = [(1, 2, 1), (1, 4, 0), (2, 5, 2),
                       (3, 4, 1), (3, 5, 2), (4, 5, 2), (4, 6, 2)]

# find the edge (as index) that ends latest but before given edge (by index) starts
# TODO : I think we can reduce the indexes from to (l and r) to one (check
# cases)


def binary_search(l: int, r: int, original_e: tuple, edges: list) -> int:
    if r > l:
        mid = l + (r - l) // 2
        if mid == 0:
            return 0  # none found maps to edge 0 with value 0

        if edges[mid][1] == original_e[0]:  # edge ends before original starts
            return mid

        elif edges[mid][1] < original_e[0]:  # is valid -> go right
            return binary_search(mid, r, original_e, edges)

        else:  # is not valid -> go left
            return binary_search(l, mid, original_e, edges)
    else:
        # TODO : This might not be correct
        return 0  # index 0 will get max value 0 in weighted_scheduling


# O(n log n), returns max weight that can be scheduled
def weighted_scheduling(edges: list) -> int:
    edges.sort(key=lambda x: x[1])  # sort by endtime
    n = len(edges)

    # for each edge e_i in sorted edges store
    # that ends latest but before given edge starts
    pre = []
    for i in range(n):
        # search in the lower part
        map_to = binary_search(0, i, edges[i], edges)
        pre.append(map_to)

    M = [0]  # partial solutions table
    for j in range(1, n):
        take_edge = edges[j][2] + M[pre[j - 1]]
        dont_take_edge = M[j - 1]
        M.append(max(take_edge, dont_take_edge))  # implements the OPT function

    return M[-1]
