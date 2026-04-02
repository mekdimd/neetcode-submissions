class Solution:
    def missingNumber(self, nums: List[int]) -> int:
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