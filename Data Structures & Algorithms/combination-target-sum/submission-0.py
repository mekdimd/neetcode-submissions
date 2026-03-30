class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        nums = [3,4,5]
        tarr
        3,3,3,
        """
        
        res = []

        # keep track of each stage
        curr = []

        def backtrack(i, curr_sum):
            # found solution, add current sum to result
            if curr_sum == target:
                res.append(curr.copy())
                return
            
            # edge cases, idx i done or sum is too large
            if i >= len(nums) or curr_sum > target:
                return
            
            # right branch, done using i, check idx i+1
            backtrack(i+1, curr_sum)

            # left branch, consider adding i again
            curr.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            curr.pop()

        # backtrack from idx 0, with empty sum
        backtrack(0, 0)

        return res
