# 988. Smallest String Starting From Leaf

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        self.sm = None

        def dfs(node, p):
            if not node:
                return
            
            c = chr(node.val + ord('a'))
            p = c + p  
            if not node.left and not node.right:
                if self.sm is None or p < self.sm:
                    self.sm = p
                return

            dfs(node.left, p)
            dfs(node.right, p)

        dfs(root, "")
        return self.sm
