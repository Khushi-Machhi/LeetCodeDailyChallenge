# 1249. Minimum Remove to Make Valid Parentheses

class Solution(object):
    def minRemoveToMakeValid(self, s):

        s = list(s)
        stack = []

        for i, j in enumerate(s):
            if j == '(':
                stack.append(i)
            elif j == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        for index in stack:
            s[index] = ''

        return ''.join(s)
