class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None:
            return 0
        if head.next.next == None:
            return head.val + head.next.val
        
        values = []
        i = 0
        while head:
            values.append(head.val)
            head = head.next

        curMax = 0
        start = 0
        end = len(values)-1
        while end != 0:
            curMax = max(curMax, (values[start]+ values[end]))
            start += 1
            end -= 1

        return curMax