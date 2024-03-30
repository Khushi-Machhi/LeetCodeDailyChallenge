# 992. Subarrays with K Different Integers

    def subarraysWithKDistinct(self, nums, k):
        
        def atMostK(nums, k):
            counter = {}
            left = right = result = 0
            while right < len(nums):
                if nums[right] not in counter:
                    counter[nums[right]] = 0
                counter[nums[right]] += 1
                
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                
                result += right - left + 1
                right += 1
            
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)
