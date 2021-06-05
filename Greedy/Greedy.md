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

#### Interval Lateness Minimization

**Problem :**
The intervals now feature a deadline. The objective is to minimize the overall time 
between deadline and end.

**Solution :**
Choose the next interval by the earliest remaining deadline.

#### Huffman Codes

**Problem :**
Given some characters with each one being assigned some relative frequency or 
probability (they sum up to one), find a way to encode them (binary), 
so the length of an encoded string is minimal.

**Observation :**
Codes for characters can't be prefixes of eachother. Otherwise decoding would not be definitive.
So the objective is to find a prefix free encoding where small frequencies correlate with
short codes.

**Solution :**
Bottom up :
```
1 if|Σ|= 2:
2   kodiere einen Buchstaben mit 0, den anderen mit 1
3 else:
4   a,b := ”Buchstaben mit kleinster Häufigkeit“
5   lösche a und b aus Σ und füge neuen Buchstaben 'ab' hinzu
6   f('ab') := f(a) + f(b)
7   Konstruiere rekursiv prafixfreien Code mit Baum T′
8   Ersetze in T′ das Blatt 'ab' durch den Unterbaum
```