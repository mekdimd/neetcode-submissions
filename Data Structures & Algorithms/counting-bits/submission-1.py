class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Time O(N), Space O(N)
        """
        res = []

        # print bits for range [0, n] inclusive
        for num in range(n+1):
            res.append(self.countOnes(num))
        
        return res


    # O(32)
    def countOnes(self, n):
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        
        return count