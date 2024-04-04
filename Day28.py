# 1614. Maximum Nesting Depth of the Parentheses

class Solution(object):
    def maxDepth(self, s):
        m = 0
        c = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
                c += 1
                m = max(m, c)
            elif char == ')':
                stack.pop()
                c -= 1
        return m
