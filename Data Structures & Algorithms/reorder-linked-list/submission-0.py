# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = head
        while prev:
            temp = curr.next
            temp1 = prev.next
            curr.next = prev
            prev.next = temp
            curr = temp
            prev = temp1
