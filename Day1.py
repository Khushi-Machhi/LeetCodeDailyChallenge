# 3005.Count Element With Maximum Frequency

from collections import Counter
def maxFrequencyElement(nums):
    f=Counter(nums)
    freq = [i for i in f.values()]
    m=max(freq)
    c=0
    for i in freq:
        if i==m:
            c=c+i 
    return c
  
maxFrequencyElement([1,2,5,2,1,2])
