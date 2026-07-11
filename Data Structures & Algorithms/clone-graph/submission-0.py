"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # def bfs(self, seen, node):
    from collections import deque
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            nn = Node(node.val)
            oldToNew[node] = nn
            for n in node.neighbors:
                nn.neighbors.append(dfs(n))
            return nn
        
        return dfs(node) if node else None
                