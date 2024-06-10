#1051. Height Checker

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        arr = sorted(heights)
        
        c = 0
        
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                c += 1
        
        return c
