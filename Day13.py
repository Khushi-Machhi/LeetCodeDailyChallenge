# 1669. Merge In Between Linked Lists

class Solution(object):
    def mergeInBetween(self, l1, a, b, l2):
        d = ListNode(-1)
        d.next = l1
        prev_a = d
        
        for _ in range(a):
            prev_a = prev_a.next
        
        node_b = prev_a
        for _ in range(b - a + 1):
            node_b = node_b.next
        
        prev_a.next = l2
        
        tail_l2 = l2
        while tail_l2.next:
            tail_l2 = tail_l2.next
        
        tail_l2.next = node_b.next
        
        return d.next
