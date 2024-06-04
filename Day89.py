# 409. Longest Palindrome
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = set()
        for i in s:
            if i not in st:
                st.add(i)
            else:
                st.remove(i)

        n = len(s)
        m = len(st)

        if m!=0:
            return n-m+1
        else:
            return n
