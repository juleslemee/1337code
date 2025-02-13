class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        maxSum = 0
        first, second = head, prev

        while second:
            maxSum = max(maxSum, first.val + second.val)
            first = first.next
            second = second.next

        return maxSum