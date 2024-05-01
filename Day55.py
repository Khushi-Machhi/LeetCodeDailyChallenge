# 2000. Reverse Prefix of Word

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        
        i = word.index(ch)
        l, r = 0, i
        arr = list(word)
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return ''.join(arr)
