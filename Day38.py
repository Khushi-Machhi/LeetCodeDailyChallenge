# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def leaf(node):
            return node and not node.left and not node.right
        
        if not root:
            return 0
        
        lsum = 0
        
        if leaf(root.left):
            lsum += root.left.val
        else:
            lsum += self.sumOfLeftLeaves(root.left)
            
        lsum += self.sumOfLeftLeaves(root.right)  
        
        return lsum
        
