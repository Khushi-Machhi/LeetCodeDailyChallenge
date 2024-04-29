# 2997. Minimum Number of Operations to Make Array XOR Equal to K

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        xor = 0
        for i in nums:
            xor ^= i
        
        target_xor = xor ^ k
        
        ans = 0
        while target_xor:
            ans += target_xor & 1
            target_xor >>= 1
        
        return ans

        
        
        
