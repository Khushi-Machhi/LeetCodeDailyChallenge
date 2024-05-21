# 78. Subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def func(i,p):
            if i == len(nums):
                subsets.append(p[:])
                return

            p.append(nums[i])
            func(i+1,p)
            p.pop()

            func(i+1,p)
        subsets = []
        func(0,[])
        return subsets    
        
