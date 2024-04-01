# 58. Length of Last Word

    def lengthOfLastWord(self, s):
        length = 0
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                return length
        
        return length
        
