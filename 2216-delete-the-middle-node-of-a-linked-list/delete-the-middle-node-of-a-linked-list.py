# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init two pointers and previous node than the one we'll treat
        slow = head
        fast = head
        prev = None

        if head.next == None:
            return None
        
        if head.next.next == None:
            head.next = None
            return head
        
        # iterate we get to the end with fast
        while fast and fast.next:
            fast = fast.next.next # move by two
            prev = slow # set prev to slow before we move it
            slow = slow.next # move by one
        
        prev.next = slow.next # should skip slow (the one after)

        return head


