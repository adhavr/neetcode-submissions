# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root, depth):
        count = depth + 1
        if root.left:
            count = max(self.bfs(root.left, depth+1), count)
        if root.right:
            count = max(self.bfs(root.right, depth+1), count)
        return count
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.bfs(root, 0)