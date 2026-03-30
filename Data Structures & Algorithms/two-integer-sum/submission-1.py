class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store target - current with index
        diff = {}

        for i, num in enumerate(nums):
            # number found
            if num in diff:
                return [diff[num], i]

            # insert number if not seen
            diff[target-num] = i

        # pair is guaranteed, should never hit this case
        return []