# 2441. Largest Positive Integer That Exists With Its Negative

class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        k = -1
        
        for num in nums:
            if -num in a:
                k = max(k, abs(num))
            a.add(num)
        
        return k
        
