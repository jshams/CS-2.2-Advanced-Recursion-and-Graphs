# Knapsack Problem:
## What is the problem?
- You are given a bunch of items
- Each item has a weight and value
- You also have a knapsack which has a maximum capacity
- The goal is to find the best combinations of items (based on their value, that also fit in the bag)

## How do we solve it?
- We can use brute force to try every combination and find which has the best value and fits in the bag
- This is a naive approach because sometimes we'll have combinations appear multiple times
- This is where we can apply dynamic programming so we won't have to repeat tasks

## What is dynamic programming?
- Dynamic programming is a more optimized version of recursion
- If we ever see any subproblems that get repeated we can do them only once by storing their results.

## 5 steps of dynamic programming:
- Identify the subproblems
    - In our knapsack a subproblems are combinations that repeat
- Guess first choice
    - we can store them in a dictionary
- Recursively define the value of an optimal solution:
    - 

