### Algorithm Theory <hr />

#### About this project
This is supposed to be a place where I can learn about algorithms,
document this knowledge and test my understanding by implementing them and if it helps anyone else I consider that a win-win.

#### Algorithm  overview

The following list tracks which algorithms have been included and which are planned. Don't hesitate to suggest more !

1. **Greedy Algorithms**
- [x] Interval Scheduling 
- [x] Interval Partitioning
- [x] Interval Lateness Minimization
- [x] Dijkstra
- [x] Minimal Span Trees (MST)
- [x] Huffman Codes

2. **Divide and Conquer**
- [x] Counting Inversions
- [x] Closest Pair
- [ ] Matrix Multiplication
- [ ] Fast Fourier Transformation (FFT)

3. **Dynamic Programming**
- [x] Weighted Interval Scheduling
- [ ] Knapsack
- [ ] Longest Common Subsequence
- [ ] Shortest Paths (revisited: Bellman Ford)
- [ ] Detection of negative circles 

4. **Flow Graphs**
- [ ] Maximum Flow (Ford-Fulkerson)
- [ ] Circulation in flow graphs

#### Structure

`src` contains the modules for the various types of algorithms.
Each of the modules is accompanied by a corresponding `.md` file with short explanations and examples on the algorithms. (very much WIP)
Furthermore there is a `utils.py`, which at the moment just contains visualization helpers for graphs and intervals. 

modules may be imported from the package like this
`from AlgorithmTheory import DivideAndConquer`

`tests`, as you might've guessed, contains the testsuite.
 For each module in `src` there is a testing module in `tests/modules`.
 Furthermore there is a `Context.py` to import the src modules.
 This part of the structure can probably be improved a lot.

#### Tools

**Formatting :**

autopep8, which can be installed from pip with `pip install autopep8`.

run from the root of the directory with:
`autopep8 --in-place --aggressive --recursive .`

**Printing Graphs :**

graphviz, which can be installed with `pip install graphviz` but it's only needed for the corresponding utils function.
