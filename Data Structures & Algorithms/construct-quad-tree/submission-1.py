"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        m = len(grid[0])

        if n == 1:
            return Node(grid[0][0], 1, None, None, None, None)
        
        topLeft = self.construct([row[:m // 2] for row in grid[:n // 2]])
        topRight = self.construct([row[m // 2:] for row in grid[:n // 2]])
        bottomLeft = self.construct([row[:m // 2] for row in grid[n // 2:]])
        bottomRight = self.construct([row[m // 2:] for row in grid[n // 2:]])

        if topLeft.isLeaf == 1 and topRight.isLeaf == 1 and bottomLeft.isLeaf == 1 and bottomRight.isLeaf == 1 \
            and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, 1, None, None, None, None)
        
        return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
