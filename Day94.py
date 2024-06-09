# 974. Subarray Sums Divisible by K

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        remainder_c = {0: 1}  
        c = 0
        
        for num in nums:
            s += num
            remainder = s % k
            
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_c:
                c += remainder_c[remainder]
                remainder_c[remainder] += 1
            else:
                remainder_c[remainder] = 1
        
        return c
