#  1442. Count Triplets That Can Form Two Arrays of Equal XOR
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        xor_arr = [0] * (n + 1)
        for i in range(n):
            xor_arr[i + 1] = xor_arr[i] ^ arr[i]

        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if xor_arr[i] == xor_arr[k + 1]:
                    count += k - i

        return count

