class Solution(object):
    def isSameTree(self, p, q):
        
        def same(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
        return same(p, q)