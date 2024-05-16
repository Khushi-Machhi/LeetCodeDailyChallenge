# 2331. Evaluate Boolean Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if not root:
            return False

        if root.val == 0 or root.val == 1:
            return bool(root.val)

        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)

        if root.val == 2:
            return l or r
        elif root.val == 3:
            return l and r

        return False

        
        
