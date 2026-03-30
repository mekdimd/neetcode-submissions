class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, n in enumerate(nums):
            diff = target - n

            # Found number in lookup, return idx, i
            if diff in lookup:
                return [lookup[diff], i]
            
            # diff not found, Insert n -> i
            else:
                lookup[n] = i
        
        
        return [-1]
"""


target 7

3,4,5,6

diff = 7-5
{
    4 -> 0
    3 -> 1



}
"""