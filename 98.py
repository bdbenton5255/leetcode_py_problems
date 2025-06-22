class Solution(object):
    def isValidBST(self, root):
        def is_valid(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

        return is_valid(root, float('-inf'), float('inf'))