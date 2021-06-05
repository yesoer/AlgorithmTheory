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

