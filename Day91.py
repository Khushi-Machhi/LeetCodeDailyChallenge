# 846. Hand of Straights

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        hand_count = Counter(hand)

        sorted_keys = sorted(hand_count.keys())
        
        for card in sorted_keys:
            if hand_count[card] > 0:
                num_needed = hand_count[card]

                for i in range(groupSize):
                    if hand_count[card + i] < num_needed:
                        return False
                        
                    hand_count[card + i] -= num_needed
        
        return True
        
