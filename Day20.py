# 713. Subarray Product Less Than K

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k <= 1:
            return 0
        
        c = 0
        product = 1
        left = 0
        
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            c += right - left + 1
        
        return c

        
