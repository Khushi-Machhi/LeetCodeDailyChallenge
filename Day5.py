# 1171. Remove Zero Sum Consecutive Nodes from Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
    
        i = ListNode(0)
        i.next = head
        sum = 0
        sums = {0: i}
        current = head

        while current:
            sum += current.val
            sums[sum] = current
            current = current.next

        sum = 0
        current = i
        while current:
            sum += current.val
            if sum in sums:
                current.next = sums[sum].next
            current = current.next

        return i.next
