# 950. Reveal Cards In Increasing Order

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        result = [0] * n
        queue = list(range(n))

        for card in deck:
            result[queue.pop(0)] = card
            if queue:
                queue.append(queue.pop(0))

        return result
