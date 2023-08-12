"""

FILL A 2D MATRIX WITH SHORTEST PATHS

Given a 2D matrix n*m size, find the shortest path to the gates and not jumping over the walls

- unfilled cells : 0
- walls : -1
- gates : -2

Example:

Input = [
  [0, 0, -1, -2]
  [0, 0,  0,  0]
]

Ouptput = [
  [5, 4, -1, -2]
  [4, 3,  2,  1]
]

Input = [
  [0,  0, -1, -2]
  [-2, 0,  0,  0]
]

Ouptput = [
  [1,  2, -1, -2]
  [-2, 1,  2,  1]
]

"""
