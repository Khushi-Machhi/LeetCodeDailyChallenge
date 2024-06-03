# 2486. Append Characters to String to Make Subsequence

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i , j =  0 , 0
        n , m = len(s),len(t)

        while i<n and j<m :
            if s[i]==t[j]:
                j+=1
            i+=1
            
        res = m-j
        return res
        
