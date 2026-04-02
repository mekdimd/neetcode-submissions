class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """

        calcualte xor for 1^2^...^n

        then for each value in arr, xor. result will be the missing number

        e.g. (1^1) ^ (2^2) ^ ...^ 3 ^... ^ (4^4) ^ .... (n^n)

        one number will not be XORed with itself, and therefore not cancel out

        """

        # xor = 1^2^...^n
        xor = 0
        for i in range(len(nums)+1):
            xor ^= i
        

        # xor = (1^1) ^ (2^2) ^ ... 3  ... 
        for n in nums:
            xor ^= n
        
        # remaning number will be result
        return xor

    def math_approach(self, nums):
        """
        sum [0,n] = n(n+1) / 2

        O(N) time
        O(1) space
        """

        n = len(nums)

        expected = (n * (n+1)) // 2

        actual = 0
        for n in nums:
            actual += n
        
        return expected - actual