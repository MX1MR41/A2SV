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
        # dfs
        # keep dividing the grid into four quadrants until you have only one cell which is base case
        # build up from there

        # corners: topLeft = [row][col], topRight = [row][col + dist], 
        # bottomLeft = [row + dist][col], bottomRight = [row + dist][col + dist]
        def quad(row, col, dist):
            if dist == 0: # a single cell
                node = Node(grid[row][col], True, None, None, None, None)
                return node

            dist //= 2

            topLeft = quad(row, col, dist)
            topRight = quad(row, col + dist, dist)
            bottomLeft = quad(row + dist, col, dist)
            bottomRight = quad(row + dist, col + dist, dist)

            allLeaves = topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf

            allSameValues = topLeft.val == topRight.val == bottomLeft.val == bottomRight.val


            if allLeaves and allSameValues: # we cam make this node itself a leaf and discard the rest
                node = Node(topLeft.val, True, None, None, None, None)
            else:
                node = Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

            return node

        return quad(0, 0, len(grid))
