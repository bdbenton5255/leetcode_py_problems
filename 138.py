class Solution(object):
    def copyRandomList(self, head):
        if not head: return None

        cur = head
        old_to_new = {}

        while cur:
            node = Node(x=cur.val)
            old_to_new[cur] = node
            cur = cur.next

        cur = head
        while cur:
            new_node = old_to_new[cur]
            new_node.next = old_to_new[cur.next] if cur.next else None
            new_node.random = old_to_new[cur.random] if cur.random else None
            cur = cur.next
        
        return old_to_new[head]