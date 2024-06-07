# 648. Replace Words

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        dictionary.sort(key=len)
        
        words = sentence.split()
       
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        
        return ' '.join(words)
        
