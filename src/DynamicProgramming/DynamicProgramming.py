test_weighted_edges = [(1, 2, 1), (1, 4, 0), (2, 5, 2),
                       (3, 4, 1), (3, 5, 2), (4, 5, 2), (4, 6, 2)]

def binary_search(l: int, r: int, original_i: tuple, intervals: list) -> int:
    """
    Find the interval (as index) that ends latest but before given interval
    original_i starts in O(log n) where n is the difference r - l
        Parameters:
            l(int): the leftmost index to consider
            r(int): the rightmost index to consider
            original_i(tuple): an interval as (start, end, weight)
            intervals(list): a list of intervals as (start, end, weight)
            
        Returns:
            binary_search(int): index of the latest interval that doesn't overlap 
                                with original_i, or None if no interval ends before
                                original_i starts
    """
    if r >= l:
        mid = l + (r - l) // 2

        if intervals[mid][1] == original_i[0]:  # interval ends when original starts
            return mid

        elif intervals[mid][1] < original_i[0]:  # is valid -> go right
            possibly_closer = binary_search(mid+1, r, original_i, intervals)
            return possibly_closer if possibly_closer else mid

        else:  # is not valid -> go left
            return binary_search(l, mid-1, original_i, intervals)
    else:


# O(n log n), returns max weight that can be scheduled
def weighted_scheduling(edges: list) -> int:
    edges.sort(key=lambda x: x[1])  # sort by endtime
    n = len(edges)

    # for each edge e_i in sorted edges store
    # that ends latest but before given edge starts
        return None  # no exact match found
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
