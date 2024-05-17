# 1325. Delete Leaves With a Given Value


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def d_f_s(node):
            if node is None:
                return None

            node.left = d_f_s(node.left)
            node.right = d_f_s(node.right)

            if node.left is None and node.right is None and node.val == target:
                return None

            return node

        return d_f_s(root)
