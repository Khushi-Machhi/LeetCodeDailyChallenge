# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        l=list()
        x=head
        while x:
            l.append(x.val)
            x=x.next
        
        n=len(l)
        for i in range(n//2):
            if l[i]==l[n-i-1]:
                i+=1
            else:
                return False
        return True
