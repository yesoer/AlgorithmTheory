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
        return None  # no exact match found

def weighted_scheduling(intervals: list) -> int:
    """
    O(n log n) scheduling weighted intervals
        Parameters:
            intervals(list): intervals to schedule as (start, end, weight)
            
        Returns:
            max_weight(int): max weight that can be scheduled
    """
    intervals.sort(key=lambda x: x[1])  # sort by endtime
    n = len(intervals)

    # for each interval intervals[i] store
    # that ends latest but before given one starts
    pre = []
    for i in range(n):
        # search in the lower part
        map_to = binary_search(0, i, intervals[i], intervals)
        pre.append(map_to)

    M = []  # partial solutions table
    for j in range(0, n):
        # get the most weight scheduled for the latest interval before j
        pre_j = M[pre[j]] if pre[j] != None else 0

        take_j = intervals[j][2] + pre_j # weight if j is included
        valid_index = j-1 > 0 and j-1 < len(M)
        dont_take_j = M[j-1] if valid_index else 0 # if j is not included

        M.append(max(take_j, dont_take_j))  # implements the OPT function

    max_weight = M[-1] if len(M) > 0 else 0
    return max_weight
