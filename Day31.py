# 678. Valid Parenthesis String

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = j = 0
        for c in s:
            if c == '(':
                i += 1
                j += 1
            elif c == ')':
                if i > 0:
                    i -= 1
                j -= 1
            else:  
                if i > 0:
                    i -= 1
                j += 1
            if j < 0:  
                return False
        return i == 0
