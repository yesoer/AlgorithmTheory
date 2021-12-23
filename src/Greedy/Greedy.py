############
# Intervals
############

test_intervals = [(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]


def interval_scheduling(intervals: list) -> list:
    """
    Interval Scheduling in O(n log n).
        Parameters:
            intervals(list): list of tuples representing jobs as (start, end)
            
        Returns:
            timeline(list): list of chosen intervals
    """
    if intervals == []:
        return []

    intervals.sort(key=lambda x: x[1])  # sort by increasing endtime
    timeline = [ intervals[0] ]

    for next_i in intervals[1:]:
        if next_i[0] >= timeline[-1][1]:  # no overlapping
            timeline.append(next_i)

    return timeline

# TODO : check if the inner loop pushes this out of O(n log n)
def interval_partitioning(intervals: list, check=False) -> list:
    """
    Interval Partitioning in O(n log n)
        Parameters:
            intervals(list): list of tuples representing jobs as (start, end)
            check(boolean): check against result of max_overlap (defaults to false)
            
        Returns:
            timelines(list): list of chosen intervals, per machine
    """
    if intervals == []:
        return []

    intervals.sort(key=lambda x: x[1])  # sort by endtime
    timelines = [ [intervals[0]] ]

    for next_i in intervals[1:]:
        appended = False

        # try fitting next_i into existing timeline
        for t in range(len(timelines)):
            if next_i[0] >= timelines[t][-1][1]:  # no overlapping
                timelines[t].append(next_i)
                appended = True
                break

        if not appended:  # create a new timeline
            timelines.append([next_i])

    if check and len(timelines) != max_overlap(intervals):  # check correctness
        print("Something doesn't work like it's supposed to")
        return None

    return timelines


def max_overlap(intervals: list) -> int:
    """
    Helper running in O(n log n)
        Parameters:
            intervals(list): list of tuples representing jobs as (start, end)
            
        Returns:
            max_overlap(int): maximum number of overlapping jobs
    """

    # flatten intervals into one timeline
    end_values = [ { "val": i[1], "type": "end"} for i in intervals]
    start_values = [ { "val": i[0], "type": "start"} for i in intervals]

    all_values = start_values + end_values
    # sort by increasing time first and secondly end first
    # thereby if start of i matches end of j, the end is processed 
    # first and it is not counted as an overlap
    all_values.sort(key=lambda x: (x["val"], 1 if x["type"] == "start" else 0))

    # iterate over timeline and increase/decrease overlap,
    # when there is a start/end
    curr_overlap = 0
    max_overlap = 0
    for v in all_values:
        if v["type"] == "start":
            curr_overlap += 1
        else:
            curr_overlap -= 1

        max_overlap = max(curr_overlap, max_overlap)

    return max_overlap


############
# Frequencies
############

test_frequencies = [('m', 2 / 11), ('i', 4 / 11), ('s', 4 / 11), ('p', 1 / 11)]


def huffman_wrapper(frequencies: list, check=False) -> dict:
    """
    Wraps actual huffman_code() to get the dict for the input aswell
        Parameters:
            frequencies(list): list of tuples : (character, frequency)
            
        Returns:
            huffman_codes(dict): computed huffman codes, as { char: binary }
    """
    
    # map frequencies to a higher space to avoid floating point errors
    frequencies = [(x,y * 100) for x,y in frequencies] 

    # sort by frequency
    frequencies.sort(key=lambda x: x[1])

    # key:value , char:empty string
    frequencies_d = {f[0]: "" for f in frequencies}

    huffman_codes = huffman_code(frequencies, frequencies_d)

    if check:
        return None if not prefix_free(huffman_codes) else huffman_codes

    return huffman_codes

def huffman_code(frequencies_l: list, frequencies_d: dict) -> dict:
    """
    O(?) recursion has #character depth
        Parameters:
            frequencies_l(list): list of tuples (character, frequency) 
                                 ,sorted by the latter
            frequencies_d(dict): dict, which maps each character to the empty list
            
        Returns:
            huffman_codes(dict): computed huffman codes, as { char: binary }
    """

    # recursion anker, if frequency is one that means
    #  all characters and frequencies are merged
    if len(frequencies_l) == 1:
        return frequencies_d

    # elements to be merged are those with the smallest frequency
    key_smallest = frequencies_l[0][0]
    key_second_smallest = frequencies_l[1][0]

    # simulate the hirarchy in the tree so add a leading
    # 1 or 0 to all the children in the corresponding subtree
    # reminder: 'key' consists of one or more (!) characters
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

    huffman_codes = huffman_code(new_frequencies, frequencies_d)
    return huffman_codes

def prefix_free(huffman_codes: dict) -> bool:
    """
    O(n²) Checks if the assigned huffman codes are prefix free/valid
        Parameters:
            huffman_codes(list): huffman codes, as { char: binary }
            
        Returns:
            prefix_free(bool): whether all assigned codes are prefix free from eachother
    """
    for char, binary in huffman_codes.items():
        for comp_char, comp_binary in huffman_codes.items():
            if (char != comp_char and
                    len(binary) < len(comp_binary) and
                    binary == comp_binary[:len(binary)]):
                return False
    
    return True

def insert_sort(l: list, elem, key=None, order=lambda x, y: x >= y) -> list:
    """
        Insertion Sort/Insert in O(n)
        Parameters:
            l(list): list with elements of type T
            elem(T): element to insert
            key: key for accessing compare property of T (default: None)
            order(lambda): compare function for T[key] (default: >=)
            
        Returns:
            l(list): l with inserted elem
    """
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
test_edges = [(0, 1, 0.5), (1, 3, 5), (1, 2, 2), (2, 4, 1), (0, 4, 10)]
test_vertices = [0, 1, 2, 3, 4]


def graph_from_list(vertices: list, edges: list, directed=False) -> dict:
    """
    O(|V| + |E|) Helper to get graph (=dict) from input in O(n)
        Parameters:
            vertices(list): list of vertices
            edges(list): representing edges as [(start, end, ...)]
            directed(boolean): whether the graph is directed (default: false)
            
        Returns:
            v_e_map(dict): graph as { vertex: [edge with that vertex] }
    """
    v_e_map = {v: [] for v in vertices}

    for e in edges:
        v_e_map[e[0]].append(e)
        if not directed:
            v_e_map[e[1]].append(e)

    return v_e_map


def dijkstra(graph: dict, start, end) -> (list, float):
    """
    Dijkstra in O((|V| + |E|) log |V|)
        Parameters:
            graph(dict): graph as { vertice: [edge with vertice] }
            start(list): start vertex
            end(boolean): end vertex
            
        Returns:
            path(list): path from s to t as edges (start, end, weight)
            dist_s_t(float): distance for that path
    """
    # distance to each vertex t from vertex s
    dist_s_t = [float("inf")] * len(graph.keys())
    dist_s_t[start] = 0

    # for each vertex, store the last one on the shortest path to them
    prev_t = [None] * len(graph.keys())
    
    # unvisited vertices
    to_process = {t for t in graph.keys()} 
    
    # traverse bfs like
    while to_process:

        # coose next vertex by minimal distance
        # out of unvisited ones
        curr = None
        for v in to_process:
            if curr == None or dist_s_t[curr] > dist_s_t[v]:
                curr = v
        
        # if this is true, end is visited and we definitely
        # have found the shortest path
        if curr == end:
            break;

        to_process.remove(curr) # mark vertex as visited

        # for each neighbor that has not been visited
        for edge in graph[curr]:
            neighbor = edge[0] + edge[1] - curr
            if neighbor in to_process:

                # if the possible distance is less than before, update
                new_dist = dist_s_t[curr] + edge[2]
                if new_dist < dist_s_t[neighbor]:
                    dist_s_t[neighbor] = new_dist
                    prev_t[neighbor] = curr

    # trace the path from end to start
    path = []
    prev = end
    while prev != None:
        path.append(prev)
        prev = prev_t[prev]

    return path, dist_s_t[end]

# TODO : 'in' has O(n), use dicts for O(1)
def mst_kruskal(vertices: list, edges: list) -> list:
    """
    MST Kruskal
        Parameters:
            vertices(list): list of vertices
            edges(list): list of edges (start, end, weight)
            
        Returns:
            reduced_edges(list): list of edges (start, end, weight) for mst
    """
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
    """
    MST Prim
        Parameters:
            graph(dict): graph as { vertice: [edge with vertice] }
            
        Returns:
            reduced_edges(list): list of edges (start, end, weight) for mst
    """
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
