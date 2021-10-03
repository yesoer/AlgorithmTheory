### Algorithm Theory <hr />

#### About this project
This is supposed to be a place where I can learn about algorithms,
document this knowledge and test my understanding by implementing them.

#### Algorithm  overview

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

modules may be imported from the package like this
`from AlgorithmTheory.src.DivideConquer import DivideAndConquer`
if you really need to but this repository should not be thought of as
an efficient algorithm library (yet, who knows).

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

graphviz, which can be installed with `pip install graphviz`.
