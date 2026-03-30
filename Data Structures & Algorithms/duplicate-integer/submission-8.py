class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        METHOD 1: set way
        TIME: O(N)
        SPACE: O(N)
        """
        seen = set()

        for n in nums:
            # add each item in arr to our set
            seen.add(n)
        
        # check if the sizes are different
        # if there is a duplicate, the set will have smaller length
        return len(seen) != len(nums)

        """
        METHOD 2: HASHMAP
        TIME: O(N)
        SPACE: O(N)
        
        nums = [1, 2, 3, 3]

        {
            1: 1
            2: 1
            3: 1
        }
        """
        # seen_map = {}

        # for n in nums:
        #     # if key not present
        #     if n not in seen_map.keys():
        #         seen_map[n] = 1
        #     else:
        #         return True
        
        # return False
                


         


        