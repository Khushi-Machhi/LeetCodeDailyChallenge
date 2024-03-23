# 143. Reorder List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        curr = s
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first_half = head
        second_half = prev
        while second_half.next:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp

            temp = second_half.next
            second_half.next = first_half
            second_half = temp

        return head
