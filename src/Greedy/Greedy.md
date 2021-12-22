## Greedy Algorithms

### Intervals <hr />

#### Interval Scheduling

**Problem :**
From a number of jobs with start and end time choose a subset such that none are 
overlapping and as many are processed as possible.

**Solution :**
Choose the next interval to include by their endtime, earlier ones being the preference.
Since the result should be none overlapping one should only consider those where the starting time is larger than the 
endtime of the lastly chosen Interval.

**Runtime Complexity :**
The sorting takes O(n log n). After that we only need to iterate over this sorted list, which gives us O(n) for that part and thereby O(n log n) in total.

#### Interval Partitioning

**Problem :**
Find the least number of timelines necessary such that no intervals overlap.

**Solution :**
It's equal to the max number of overlapping intervals.
One could also process one after another and if they don't fit into an existing timeline, 
a new one should be created. 

**Runtime Complexity :**
The sorting takes O(n log n). After that we only need to iterate over this sorted list, which gives us O(n) for that part and thereby O(n log n) in total.

#### Interval Lateness Minimization

For this problem we will be looking at intervals of the form (duration, deadline). Therefore no overlap has to be considered.

**Problem :**
The intervals now feature a deadline. The objective is to minimize the overall time 
between deadline and end.

**Solution :**
Choose the next interval by the earliest remaining deadline.
Since we don't have to consider overlap, this is actually the whole algorithm.

**Runtime Complexity :**
O(n log n)

### Graphs <hr />

#### Dijkstra

**Problem :**
In a directed Graph, where edges have weights/lengths, find the shortest path 
(minimizing the summed up length/weight) between two vertices s and t.

**Solution :**
Use BFS (see below) to calculate all distances.

BFS means visiting nodes layer by layer 
(so all neighbourse of s, then all neighbours of those etc.)

#### Minimal Span Trees (MST)

**Problem :**
In an undirected graph with weighted edges, find the minimal span tree 
(a tree that contains all nodes of the original graph), with minimal 
meaning to minimize the sum of weights of used edges.

**Solution :**
Kruskal :
Choose the edge with the least weight next, whilst not creating circles

Prim :
Start at some node and from that one forward always choose the connected edge 
with the least weight.

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
Build a tree by always choosing the two elements with the smallest frequency.
These two are now assigned a parent which in turn is assigned the combined frequency (i.e. if the elements d, c with fequencies 0.1 and 0.2 are combined, their parent dc has the frequency 0.3).
For the next iteration the two elements are disregarded but their parent is taken into consideration.
Therefore over time all elements will be concatenated and the root of the tree should have a frequency of 1.
Assigning 1 and 0 to the two edges going down from each parent gives us paths of 1s and 0s to each leaf (= individual characters). Those paths are the prefix free codes.

![Huffman_Example](https://upload.wikimedia.org/wikipedia/commons/7/74/Huffman_coding_example.svg)
By Alessio Damato - self-made  This W3C-unspecified vector image was created with Inkscape ., CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=2123492

The code provided here will **not** produce this exact result because it has no clue about what path goes right and which goes left. It assigns 0 to the smaller frequency child and 1 to the other, which still yields a correct result though.
