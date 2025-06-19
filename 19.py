class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next
        return dummy.next