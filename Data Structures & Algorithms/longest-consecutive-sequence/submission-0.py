class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        12345

        012 6789 - finding min wont work
        """


        s = set(nums)
        max_seq = 0
        for i, num in enumerate(nums):
            count = 1
            
            # continually check if next sequence is in set
            j = 1
            while num+j in s:
                count += 1
                j += 1
            
            max_seq = max(count, max_seq)
        
        return max_seq