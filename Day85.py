#  260. Single Number III

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor_result = 0
        for num in nums:
            xor_result ^= num
       
        diff_bit = xor_result & (-xor_result)
    
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
