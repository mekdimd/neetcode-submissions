class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            # pick new candidate
            if count == 0:
                res = n
            
            # update count for current candidate
            count = count+1 if res == n else count-1
        
        return res

        