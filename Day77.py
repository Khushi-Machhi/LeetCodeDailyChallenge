# 2597. The Number of Beautiful Subsets

class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def func(nums,b,j):

            if j < len(nums):
                res = func(nums,b,j+1)
                if nums[j] - k not in b:
                    res += func(nums,b+[nums[j]],j+1)
                return res

            return len(b)>0

        return func(sorted(nums),[],0)





        
