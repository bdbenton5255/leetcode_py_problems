class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        carry, current = 0, dummy_head

        while l1 or l2 or carry:
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, value = divmod(sum_, 10)
            current.next = ListNode(value)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next