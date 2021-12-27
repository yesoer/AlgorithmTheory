import copy

test_nums = [2, 3, 4, 6, 5]

def inversions(nums: list) -> int:
    """
    Counts inversions in a list of numbers recursively (not optimized !)
        Parameters:
            nums(list): the number list to count the inversions on
            
        Returns:
            inv_cnt(int): the total inversion count for the supplied number list
    """
    # recursion anker
    if 1 == len(nums):
        return 0

    # split list
    mid_i = len(nums) // 2
    inv_cnt = 0

    # count inversions between lists
    for i in range(mid_i):
        for j in range(mid_i, len(nums)):
            if nums[i] > nums[j]:
                inv_cnt += 1

    inv_cnt += inversions(nums[:mid_i])
    inv_cnt += inversions(nums[mid_i:])
    return inv_cnt


test_points = [(1, 3), (1, 2), (3, 1), (2, 2), (5, 6)]

def shortest_distance_wrapper(points: list) -> float:
    """
    Find shortest distance between n datapoints in O(n (log n)²)
        Parameters:
            points(list): the list of points as (x, y)
            
        Returns:
            short_dist(float): the shortest distance value
    """
    p_sort_y = copy.deepcopy(points)
    p_sort_y.sort(key=lambda p: p[1])

    points.sort(key=lambda p: p[0])
    p_sort_x = points

    return shortest_distance(p_sort_x, p_sort_y)


def shortest_distance(p_sort_x: list, p_sort_y: list) -> float:
    """
    Recursive shortest-distance-finder
        Parameters:
            p_sort_x(list): the list of points (x, y), sorted by x
            p_sort_y(list): the list of points (x, y), sorted by y
            
        Returns:
            min_(float): the shortest distance value
    """
    # recursion anker
    if 1 == len(p_sort_x):
        return float("inf")

    if 2 == len(p_sort_x):
        return dist(p_sort_x[0], p_sort_x[1])

    # split list
    mid_i = len(p_sort_x) // 2

    # recursively determine minimum distance in subgroups
    r_min_dist = shortest_distance(p_sort_x[mid_i:], p_sort_y)
    l_min_dist = shortest_distance(p_sort_x[:mid_i], p_sort_y)
    min_dist = min(r_min_dist, l_min_dist)

    # determine middle strip
    stripP = []
    stripQ = []
    for i in range(len(p_sort_x)):
        if abs(p_sort_x[i][0] - p_sort_x[mid_i][0]) < min_dist:
            stripP.append(p_sort_x[i])
        if abs(p_sort_y[i][0] - p_sort_x[mid_i][0]) < min_dist:
            stripQ.append(p_sort_y[i])

    # calculate min dist in strip and compare with min dist
    stripP.sort(key=lambda point: point[0])  # <-- REQUIRED
    min_a = min(min_dist, stripClosest(stripP, len(stripP), min_dist))
    min_ = min(min_a, stripClosest(stripQ, len(stripQ), min_dist))

    # return overall minimum
    return min_


def dist(p1: tuple, p2: tuple) -> float:
    """
    Helper for calculating euclidean distance between two points
        Parameters:
            p1(tuple): the first point as (x, y)
            p2(tuple): the second point as (x, y)
            
        Returns:
            return(float): the distance
    """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def stripClosest(strip: list, size: int, d: float) -> float:
    """
    Find the shortest distance
        Parameters:
            strip(list): the stripnto look at 
            size(int): the strips size
            d(float): the current minimum distance
            
        Returns:
            min_val(float): the maybe updated minimum distance
    """
    # minimum distance as d
    min_val = d

    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # It is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1]
                            - strip[i][1]) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val
