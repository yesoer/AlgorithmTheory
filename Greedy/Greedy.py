test_intervalls = [(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]

# O(n log n)
def intervall_scheduling(intervalls: list) -> list:
    intervalls.sort(key = lambda x: x[1]) # sort by endtime
    timeline = []

    for next_i in intervalls:
        if timeline == []:
            timeline.append(next_i)
        elif next_i[0] >= timeline[-1][1]: # no overlapping  
            timeline.append(next_i)
    
    return timeline

# O(n log n) ? worst case would be n²
def intervall_partitioning(intervalls: list, check=False) -> list:
    intervalls.sort(key = lambda x: x[1]) # sort by endtime
    timelines = []

    for next_i in intervalls:
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

    if check and len(timelines) != max_overlap(intervalls): # check correctness
        print("Something doesn't work like it's supposed to")

    return timelines

# O(n)
def max_overlap(intervalls: list):
    max_overlap = 0
    for i in intervalls:
        overlap = 0
        for j in intervalls:
            if i[0] < j[1] or j[0] < i[1] : # overlapping
                overlap += 1
        
        if max(overlap, max_overlap) == overlap:
            max_overlap = overlap
    
    return max_overlap