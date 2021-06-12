import copy 

test_nums = [ 2, 3, 4, 6, 5 ]

# O(?)
def inversions( nums: list) -> int:
    # recursion anker
    if 1 == len(nums):
        return 0
    
    # split list
    mid_i = int(len(nums) / 2)
    inv_cnt = 0

    # count inversions between lists
    for i in range(mid_i):
        for j in range(mid_i):
            if nums[i] > nums[mid_i + j]:
                inv_cnt += 1

    inv_cnt += inversions(nums[:mid_i])
    inv_cnt += inversions(nums[mid_i:])
    return inv_cnt 


test_points = [(1, 3), (1, 2), (3, 1), (2, 2), (5, 6)]

# O(n (log n)²)
def shortest_distance_wrapper(points: list) -> float:
    p_sort_y = copy.deepcopy(points)
    p_sort_y.sort(key=lambda p: p[1])

    points.sort(key=lambda p: p[0])
    p_sort_x = points

    return shortest_distance(p_sort_x, p_sort_y)

def shortest_distance(p_sort_x: list, p_sort_y: list) -> float:

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
    stripP.sort(key = lambda point: point[0]) #<-- REQUIRED
    min_a = min(min_dist, stripClosest(stripP, len(stripP), min_dist))
    min_ = min(min_a, stripClosest(stripQ, len(stripQ), min_dist))

    # return overall minimum
    return min_

def dist(p1: tuple, p2: tuple) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def stripClosest(strip, size, d) -> float:
     # minimum distance as d
    min_val = d
    
    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] -
                            strip[i][1]) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val