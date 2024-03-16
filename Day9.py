# 525. Contiguous Array

    def findMaxLength(nums):
        l=len(nums)
        maxl = 0
        c = 0
        hash_map = {0: -1}

        for i in range(l):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1

            if c in hash_map:
                maxl = max(maxl, i - hash_map[c])
            else:
                hash_map[c] = i

        return maxl
    findMaxLength([0,1])
