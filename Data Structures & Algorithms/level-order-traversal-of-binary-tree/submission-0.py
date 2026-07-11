# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ret = []
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    level.append(curr.val)
                    q.append(curr.right)
            if level: ret.append(level)
        return ret
            