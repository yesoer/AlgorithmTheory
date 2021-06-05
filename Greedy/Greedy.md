## Greedy Algorithms

### Intervals <hr />

#### Interval Scheduling

**Problem :**
From a number of jobs with start and end time choose a subset such that none are 
overlapping and as many are processed as possible.

**Solution :**
Choose the next interval to include by their endtime, earlier ones being the preference.
Of course one should only consider those where the starting time is more or equal to the 
endtime of the lastly chosen Interval.

#### Interval Partitioning

**Problem :**
Find the least number of timelines necessary so no intervals overlap.

**Solution :**
It's equal to the max number of overlapping intervals.
One could also process one after another and if they don't fit into an existing timeline, 
a new one should be created. 

