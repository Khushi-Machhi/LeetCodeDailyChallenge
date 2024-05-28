# 1208. Get Equal Substrings Within Budget

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        max_len = 0
        curr_cost = 0
        start = 0
        
        for end in range(len(s)):
           
            curr_cost += abs(ord(s[end]) - ord(t[end]))
            
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len


        
