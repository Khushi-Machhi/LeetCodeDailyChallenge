# 2370. Longest Ideal Subsequence

class Solution(object):
    def longestIdealString(self, s, k):
        dp = [0] * 27
        l = len(s)

        for i in range(l - 1, -1, -1):
            c = s[i]
            idx = ord(c) - ord('a')
            max_l = float('-inf')

            l = max((idx - k), 0)
            r = min((idx + k), 26)

            for j in range(l, r + 1):
                max_l = max(max_l, dp[j])

            dp[idx] = max_l + 1

        return max(dp)
