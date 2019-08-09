## Challenge 5
Determine if a given undirected graph is Eulerian (has an Eulerian Cycle).

**Input:** A file containing an undirected graph.

`python3 challenge_5.py graph_data.txt`

```
G
1,2,3,4,5
(1,2)
(2,3)
(3,4)
(4,5)
(1,5)
```

**Output** TRUE or FALSE

```
This graph is Eulerian: TRUE
```
### How to determine if a graph is Eulerian:
- If every vertex has an even degree a graph is Eulerian.
- To do this I create a histogram of vertices and their occurances. Once we have our histogram we can iterrate through the value counts and if they're all divisible by 2 we can return `TRUE` otherwise `FALSE`.