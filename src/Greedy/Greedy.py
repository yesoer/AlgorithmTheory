############
# Intervals
############

test_intervals = [(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]


def interval_scheduling(intervals: list) -> list:
    """Interval Scheduling in O(n log n)"""
    intervals.sort(key=lambda x: x[1])  # sort by endtime
    timeline = []

    for next_i in intervals:
        if timeline == []:
            timeline.append(next_i)
        elif next_i[0] > timeline[-1][1]:  # no overlapping
            timeline.append(next_i)

    return timeline

# TODO : check if the inner loop pushes this out of O(n log n)
def interval_partitioning(intervals: list, check=False) -> list:
    """Interval Partitioning in O(n log n)"""
    intervals.sort(key=lambda x: x[1])  # sort by endtime
    timelines = []

    for next_i in intervals:
        if timelines == []:
            timelines.append([next_i])
        else:
            appended = False
            for t in range(
                    len(timelines)):  # can any existing timeline "run" this
                if next_i[0] > timelines[t][-1][1]:  # no overlapping
                    timelines[t].append(next_i)
                    appended = True
                    break

            if not appended:  # create a new timeline
                timelines.append([next_i])

    if check and len(timelines) != max_overlap(intervals):  # check correctness
        print("Something doesn't work like it's supposed to")

    return timelines


def max_overlap(intervals: list):
    """Helper running in O(n²)"""
    max_overlap = 0
    max_interval_end = max(intervals, key=lambda x: x[1])[1]
    for t in range(max_interval_end):
        overlap = 0
        for i in intervals:
            if t >= i[0] and t <= i[1]:
                overlap += 1

        if max(overlap, max_overlap) == overlap:
            max_overlap = overlap

    return max_overlap


test_intervals_deadline = [
    (1, 3, 5), (0, 2, 3), (2, 5, 7), (3, 6, 6), (4, 6, 8)]


def interval_lateness(intervals: list, check=False) -> list:
    """O(n log n), only first line is different to interval scheduling"""
    intervals.sort(key=lambda x: x[2])  # sort by deadline
    timeline = []

    for next_i in intervals:
        if timeline == []:
            timeline.append(next_i)
        elif next_i[0] >= timeline[-1][1]:  # no overlapping
            timeline.append(next_i)

    return timeline


############
# Frequencies
############

test_frequencies = [('m', 2 / 11), ('i', 4 / 11), ('s', 4 / 11), ('p', 1 / 11)]


def huffman_wrapper(frequencies: list) -> dict:
    """Wraps actual huffman_code() to get the dict for the input aswell"""
    
    # map frequencies to a higher space to avoid floating point errors
    frequencies = [(x,y * 100) for x,y in frequencies] 

    # sort by frequency
    frequencies.sort(key=lambda x: x[1])

    # key:value , char:empty string
    frequencies_d = {f[0]: "" for f in frequencies}

    return huffman_code(frequencies, frequencies_d)


def huffman_code(frequencies_l: list, frequencies_d: dict) -> dict:
    """O(?)"""

    # recursion anker, if frequency is one == all characters and frequencies
    # are merged
    if len(frequencies_l) == 1:
        return frequencies_d

    # elements to be merged are those with the smallest frequency
    key_smallest = frequencies_l[0][0]
    key_second_smallest = frequencies_l[1][0]

    # simulate the hirarchy in the tree so add a leading
    # 1 or 0 to all the children in the corresponding subtree
    for key in key_smallest:
        frequencies_d[key] = "0" + frequencies_d[key]

    for key in key_second_smallest:
        frequencies_d[key] = "1" + frequencies_d[key]

    # merge elements with smallest frequency
    merged_freq = frequencies_l[0][1] + frequencies_l[1][1]
    merged_key = key_smallest + key_second_smallest
    merged = (merged_key, merged_freq)

    # insert the new element in the list and remove the old ones
    new_frequencies = insert_sort(frequencies_l[2:], merged, 1)

    return huffman_code(new_frequencies, frequencies_d)


def insert_sort(l: list, elem, key=None, order=lambda x, y: x >= y) -> list:
    """Insertion Sort/Insert in O(n)"""
    i = 0
    while i < len(l):  # find insert pos
        list_i_val = l[i] if not key else l[i][key]
        elem_val = elem if not key else elem[key]

        if order(list_i_val, elem_val):
            break

        i += 1

    l = l[:i] + [elem] + l[i:]  # insert
    return l


############
# Graphs
############

# edges : start, end, weight
test_edges = [(1, 2, 0.5), (2, 4, 5), (2, 3, 2), (3, 5, 1), (1, 5, 10)]
test_vertices = [1, 2, 3, 4, 5]


def graph_from_list(vertices: list, edges: list, directed=False) -> dict:
    """Helper to get graph (=dict) from input in O(n)"""
    v_e_map = {v: [] for v in vertices}

    for e in edges:
        v_e_map[e[0]].append(e)
        if not directed:
            v_e_map[e[1]].append(e)

    return v_e_map


def dijkstra(graph: dict, start, end) -> list:
    """Dijkstra in O(|V| + |E|)"""
    # paths from start to each other t with t being the keys
    cost_s_t = {x: None if x != start else 0 for x in graph}
    queue = [start]  # will hold the vertices at current and next level

    while queue != []:
        # pop next element
        curr = queue[0]
        queue = queue[1:]

        # see if one of edges from this point onwards would be beneficial for the target
        # if so the target now has a new value and should be evaluated
        for e in graph[curr]:
            if not cost_s_t[e[1]]:  # first value for this vertex
                cost_s_t[e[1]] = e[2] if not cost_s_t[e[0]
                                                      ] else cost_s_t[e[0]] + e[2]
                queue.append(e[1])
            elif cost_s_t[e[1]] > cost_s_t[e[0]] + e[2]:  # better than old value
                cost_s_t[e[1]] = cost_s_t[e[0]] + e[2]
                queue.append(e[1])

    return cost_s_t[end]

# TODO : 'in' has O(n), use dicts for O(1)


def mst_kruskal(vertices: list, edges: list) -> list:
    """MST Kruskal"""
    edges.sort(key=lambda x: x[2])  # sort by weight
    v_v_map = []  # list of connections
    reduced_edges = []  # list of not connected parts of the tree (=components)

    for e in edges:
        # if all vertices are in the new tree and connected, break
        connected = len(v_v_map) == 1
        complete = connected and len(v_v_map[0]) == len(vertices)
        if complete:
            break

        creates_circle = False
        e0_in = None
        e1_in = None

        # when this loop finishes we know which component(s) e connects or is connected to
        # and whether it's adding creates a circle
        for i in range(len(v_v_map)):
            if (e[0] in v_v_map[i]) and (e[1] in v_v_map[i]):  # no circle
                creates_circle = True
                break
            if e[0] in v_v_map[i]:  # get connected components
                e0_in = i            # won't get here twice
            if e[1] in v_v_map[i]:
                e1_in = i            # won't get here twice

        if not creates_circle:
            reduced_edges.append(e)

            # update connections
            if (e0_in is None) and (e1_in is None):
                # add the new component
                v_v_map.append([e[0], e[1]])
            elif (e0_in is not None) and (e1_in is not None):
                # connect components a and b in a
                v_v_map[e0_in] = v_v_map[e0_in] + v_v_map[e1_in]
                v_v_map = v_v_map[:e1_in] + v_v_map[e1_in + 1:]  # remove b
            elif e0_in is not None:
                v_v_map[e0_in].append(e[1])
            elif e1_in is not None:
                v_v_map[e1_in].append(e[0])

    return reduced_edges


def mst_prim(graph: dict) -> list:
    """MST Prim"""
    included_vertices = []
    nonincluded_vertices = list(graph.keys())
    reduced_edges = []

    # choose starting vertex ()which doesn't matter
    included_vertices = [nonincluded_vertices[0]]
    added_vertex = nonincluded_vertices[0]
    nonincluded_vertices = nonincluded_vertices[1:]
    possible_edges = []
    while nonincluded_vertices != []:

        # which are new possible edges :
        # old ones and for newly connected x, E(x, y) or (y, x)
        # (store position of y at index 3 after weight)
        # cannot create circle
        for e in graph[added_vertex]:
            e0_in = e[0] in included_vertices

            if e0_in:
                e += (1,)
                possible_edges = insert_sort(possible_edges, e, key=2)
            else:
                e += (0,)
                possible_edges = insert_sort(possible_edges, e, key=2)

        # remove lightest edges that create circles
        def creates_circle(x, y):
            return x in included_vertices and possible_edges[0][1] in included_vertices

        while creates_circle(possible_edges[0][0],
                             possible_edges[0][1]):  # don't add circle
            possible_edges = possible_edges[1:]
            continue

        chosen = possible_edges[0]  # choose "lightest" edge next
        reduced_edges.append(chosen)

        new_v = chosen[chosen[3]]
        # target of lightest edge is now visited
        included_vertices.append(new_v)
        nonincluded_vertices.remove(new_v)
        added_vertex = new_v

        possible_edges = possible_edges[1:]

    return reduced_edges
