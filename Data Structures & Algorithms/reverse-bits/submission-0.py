class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # get last bit
            bit = n & 1
            
            # add to res
            res = (res << 1) | bit
            
            # update n
            n >>= 1       # remove last digit

        return res