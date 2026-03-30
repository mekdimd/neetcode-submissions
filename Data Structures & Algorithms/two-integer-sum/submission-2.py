class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(N^2) time
        O(1) space
        """
        
        # n = len(nums)
        # for i in range(n):
        #     for j in range (i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # return []   # not found


        # Hashmap way - O(N) time, O(1) space
        """
        if target = 10
        [4,5,6]
        
        1. 10-4=6 not in hashmap. add mp[6] = 0
        2. 10-5=5 not in hashmap. add mp[5] = 1
        2. 10-6=4 in our hashmap
            return 4,6 i.e. 0, 2
        otherwise, we add it to our hashmap    
        {
            6: 0,
            5: 1,
        }
        """
        mp = {}
        for i, x in enumerate(nums):
            diff = target - x
            
            # check if diff exists for current x in hashmap
            if x in mp:
                return [mp[x], i]
            
            # value not seen, add (diff, idx)
            mp[diff] = i
                

        # not found should not hit
        return [-1, -1]