class Solution:   
    def bfs(self, head1, head2):
        if not head1 and not head2:
            return True
        elif head1 and not head2:
            return False
        elif head2 and not head1:
            return False
        if head1.val != head2.val:
            return False
        return self.bfs(head1.left, head2.left) and self.bfs(head1.right, head2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            if self.bfs(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)