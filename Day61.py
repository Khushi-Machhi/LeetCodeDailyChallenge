# 2816. Double a Number Represented as a Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def reverse(temp):
            prev = None
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            return prev

        rev = reverse(head)
        carry = 0
        res = ListNode(-1)
        ptr = rev
        cur = res
        while ptr or carry:
            val = ptr.val if ptr else 0
            temp = val + val + carry
            s = temp % 10
            carry = temp // 10
            newNode = ListNode(s)
            cur.next = newNode
            cur = cur.next
            ptr = ptr.next if ptr else None
        return reverse(res.next)
        

        
        
