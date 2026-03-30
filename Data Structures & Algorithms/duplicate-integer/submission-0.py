class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for n in nums:
            myset.add(n)
        
        return len(myset) != len(nums)
        