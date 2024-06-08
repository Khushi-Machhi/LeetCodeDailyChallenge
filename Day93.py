# 523. Continuous Subarray Sum

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_dict = {0: -1} 
        cumulative_sum = 0
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            if k != 0:
                r = cumulative_sum % k
            else:
                r = cumulative_sum
            
            if r in remainder_dict:
                if i - remainder_dict[r] > 1: 
                    return True
            else:
                remainder_dict[r] = i
        
        return False
