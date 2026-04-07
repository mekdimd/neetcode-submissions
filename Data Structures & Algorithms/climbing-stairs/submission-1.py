class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n=2

        1 or 2 steps

        n=1 -> 1
        n=2 -> 1,1 or 2 (2 ways)

        for step i, there are 2 possible paths
        - 1 step from step i-1
        - 2 steps from step i-2

        so memo[i-1] + memo[i-2]
        
        n=3
        [1,2,6]

        return 6
        
        """

        def top_down(n):
            # Time: O(2^n)
            # Space: O(n) (recursive call stack)
            # this is just fibbonacci

            # base case
            if n == 1 or n == 2:
                return n
            
            return top_down(n-1) + top_down(n-2)


        memo = {
            1: 1, 
            2: 2
        }

        def top_down_memo(n):
            # Time: O(n), each subproblem calculated once
            # Space: O(n), hashmap / call stack

            # current step has been compuated
            if n in memo:
                return memo[n]

            # otherwise, compute current step
            memo[n] = top_down_memo(n-1) + top_down_memo(n-2)
            return memo[n]


        def bottom_up(n):
            # edge case
            if n == 1 or n == 2:
                return n
            
            dp = [0] * n
            dp[0] = 1
            dp[1] = 2

            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
        
            return dp[n-1]


        def bottom_up_const(n):
            """
            1,2,3,5
                p c
            
            O(n) time
            O(1) space
            """
            if n == 1 or n == 2:
                return n
            
            prev = 1    # 1st step
            curr = 2    # 2nd step

            for i in range(2, n):
                tmp = prev
                
                prev = curr
                curr = tmp + curr
        
            return curr


        # return top_down(n)
        # return top_down_memo(n)
        # return bottom_up(n)
        return bottom_up_const(n)