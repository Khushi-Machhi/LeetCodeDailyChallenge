# 131. Palindrome Partitioning
class Solution(object):

    def isPali(self,s):
            return s == s[::-1]


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def d(s,start,p,result):
            if start == len(s):
                result.append(p[:])
                return
            for end in range(start,len(s)):
                if self.isPali(s[start:end+1]):
                    p.append(s[start:end+1])
                    d(s,end+1,p,result)
                    p.pop()
        result = []
        d(s,0,[],result)
        return result

        


        




        
