# 1544. Make The String Great

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        i = 0
        while i < len(s):
            if a and abs(ord(s[i]) - ord(a[-1])) == 32:
                a.pop()  
            else:
                a.append(s[i]) 
            i += 1
        
        return ''.join(a)



        # stack = []
        
        # for char in s:
        #     if stack and abs(ord(char) - ord(stack[-1])) == 32:  
        #         stack.pop()  
        #     else:
        #         stack.append(char) 
        
        # return ''.join(stack)
