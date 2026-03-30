class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        12345

        012 6789 - finding min wont work
        
        brute force, 
        O(N^2) time
        O(N) space
        
        """


        # s = set(nums)
        # max_seq = 0
        # for i, num in enumerate(nums):
        #     count = 1
            
        #     # continually check if next sequence is in set
        #     j = 1
        #     while num+j in s:
        #         count += 1
        #         j += 1
            
        #     max_seq = max(count, max_seq)
        
        # return max_seq

        """
        key insight: start of sequence == nums-1 doesn't exist in arr

        we can speed up computation
        """

        s = set(nums)
        max_seq = 0

        for i, num in enumerate(nums):
            # only check start of sequence i.e. if 10 is start, then 9 should not be present in set
            if num-1 not in s:
                count = 1
                
                # continually check if next sequence is in set
                j = 1
                while num + j in s:
                    count += 1
                    j += 1
                
                max_seq = max(count, max_seq)
        
        return max_seq

