#979. Distribute Coins in Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.TotalMoves = 0

        def traverse(t):
            if not t:
                return 0

            l = traverse(t.left)
            r =  traverse(t.right)

            balance = t.val + l + r - 1
            self.TotalMoves += abs(l) + abs(r)

            return balance

        traverse(root)
        return self.TotalMoves


        
