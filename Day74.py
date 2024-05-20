# 1863. Sum of All Subset XOR Totals

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fun(idx,curr):
            if idx == len(nums):
                return curr

            i = fun(idx+1,curr ^ nums[idx])
            e = fun(idx+1,curr)

            return i + e

        return fun(0,0)
        
