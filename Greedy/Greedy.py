test_intervals = [(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]

# O(n log n)
def interval_scheduling(intervals: list) -> list:
    intervals.sort(key = lambda x: x[1]) # sort by endtime
    timeline = []

    for next_i in intervals:
        if timeline == []:
            timeline.append(next_i)
        elif next_i[0] >= timeline[-1][1]: # no overlapping  
            timeline.append(next_i)
    
    return timeline

# O(n log n) ? worst case would be n²
def interval_partitioning(intervals: list, check=False) -> list:
    intervals.sort(key = lambda x: x[1]) # sort by endtime
    timelines = []

    for next_i in intervals:
        if timelines == []:
            timelines.append([next_i])
        else:
            for t in range(len(timelines)): # can any existing timeline "run" this
                appended = False
                if next_i[0] >= timelines[t][-1][1]: # no overlapping
                    timelines[t].append(next_i)
                    appended = True
                
            if not appended: # create a new timeline
                timelines.append([next_i])

    if check and len(timelines) != max_overlap(intervals): # check correctness
        print("Something doesn't work like it's supposed to")

    return timelines

# O(n²)
def max_overlap(intervals: list):
    max_overlap = 0
    for i in intervals:
        overlap = 0
        for j in intervals:
            if i[0] < j[1] or j[0] < i[1] : # overlapping
                overlap += 1
        
        if max(overlap, max_overlap) == overlap:
            max_overlap = overlap
    
    return max_overlap

test_intervals_deadline = [(1, 3, 5), (0, 2, 3), (2, 5, 7), (3, 6, 6), (4, 6, 8)]

# O(n log n), only first line is different to interval scheduling
def interval_lateness(intervals: list, check=False) -> list:
    intervals.sort(key = lambda x: x[2]) # sort by deadline
    timeline = []

    for next_i in intervals:
        if timeline == []:
            timeline.append(next_i)
        elif next_i[0] >= timeline[-1][1]: # no overlapping  
            timeline.append(next_i)
    
    return timeline

test_frequencies = [('m', 2/11), ('i', 4/11), ('s', 4/11), ('p', 1/11)]

def huffman_wrapper(frequencies: list) -> dict:
    frequencies.sort(key = lambda x: x[1]) # sort by frequency
    frequencies_d = {f[0]:"" for f in frequencies} # key:value , char:empty string
    return huffman_code(frequencies, frequencies_d)

# O(?), I suppose O(n) actually
def huffman_code(frequencies_l: list, frequencies_d) -> dict:
    # recursion anker, if frequency is one == all characters and frequencies are merged
    if len(frequencies_l) == 1:
        return frequencies_d

    # elements to be merged are those with the smallest frequency
    key_smallest = frequencies_l[0][0]
    key_second_smalles = frequencies_l[1][0]

    # simulate the hirarchy in the tree so add a leading 
    # 1 or 0 to all the children in the corresponding subtree
    for key in key_smallest:
        frequencies_d[key] = "1" + frequencies_d[key]
    
    for key in key_second_smalles:
        frequencies_d[key] = "0" + frequencies_d[key]
    
    # merge elements with smallest frequency
    merged_freq = frequencies_l[0][1] + frequencies_l[1][1]
    merged_key = key_smallest + key_second_smalles
    merged = (merged_key, merged_freq)

    # insert the new element in the list and remove the old ones
    new_frequencies = insert_sort(frequencies_l[2:], merged, 1)

    return huffman_code(new_frequencies, frequencies_d)

# O(n)
def insert_sort(l: list, elem, key=None):
    index = 0
    for i in range(len(l)): # find insert pos
        list_i_val = l[i] if not key else l[i][key]
        elem_val = elem if not key else elem[key]

        if list_i_val > elem_val:
            index = i
            break
      
    l = l[:index] + [elem] + l[index:] # insert
    return l
