# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, head1, head2):
        if not head1 and not head2:
            return True
        elif head1 and not head2:
            return False
        elif head2 and not head1:
            return False
        if head1.val != head2.val:
            print(head1.val, head2.val)
            return False
        return self.bfs(head1.left, head2.left) and self.bfs(head1.right, head2.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p, q)