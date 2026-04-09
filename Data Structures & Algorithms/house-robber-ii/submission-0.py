class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time: O(n)
        space: O(n) for copy
        """
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        def rob_houses(houses):
            prev, curr = 0, 0

            for n in houses:
                next = max(n + prev, curr)
                prev = curr
                curr = next
            
            return curr
        
        # Since 0, n are adjacent, we can't rob both
        # rob houses [0,n-1] or [1,n]
        return max(rob_houses(nums[:-1]), rob_houses(nums[1:]))