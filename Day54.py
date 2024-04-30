# 1915. Number of Wonderful Substrings

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = [1] + [0] * 1023 
        res = total = 0
        b = 0
        
        for char in word:
            b ^= 1 << (ord(char) - ord('a')) 
            res += c[b]  
            for i in range(10):
                res += c[b ^ (1 << i)]
            c[b] += 1 
        
        return res
        
