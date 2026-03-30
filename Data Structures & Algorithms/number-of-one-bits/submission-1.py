class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        O(N) time, O(1) space
        """

        count = 0
        while n > 0:
            # get last bit
            last_bit = n & 1

            # update count
            count = count + 1 if last_bit == 1 else count

            # right shift n (remove last bit)
            n >>= 1
        return count


