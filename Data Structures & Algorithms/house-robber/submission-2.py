class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.rob_top_down(nums)
        return self.rob_bottom_up_const(nums)
    
    
    def rob_top_down(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            # out of bounds
            if i < 0 or i >= len(nums):
                return 0

            # max value for house
            if i in memo:
                return memo[i]
                
            # rob current house or neighbour
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        return dfs(0)


    def rob_bottom_up(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        memo = [0] * n

        for i in range(n-2):
            memo[i] = max(nums[i] + nums[i+2], nums[i+1])

        return memo[-1]


    def rob_bottom_up_const(self, nums: List[int]) -> int:
        """
        [rob1, rob2, n, n+1, ...]
                     ^ next house
        - either dont rob next house (max val is rob2)
        - or do curr house + prev neighbour (n + rob1)

        O(n) time
        O(1) space
        """
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2