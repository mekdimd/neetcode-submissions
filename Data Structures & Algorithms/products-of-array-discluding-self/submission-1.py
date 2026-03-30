class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        naive
        
        O(N^2) time, 2 loops
        O(N) space

        """
        
        # res = []

        # for curr_idx in range(len(nums)):

        #     # calculate product
        #     product = 1
        #     for j, num in enumerate(nums):
        #         if j != curr_idx:
        #             product *= num
        
        #     # add product
        #     res.append(product)
        
        # return res

        """ 
        better
        O(N) time
        O(N) space
        """

        res = []
        
        """
        for [-1,0,1,2,3]
        
        prefix loop 
        nums: [1,-1,0,0,0]
        p = 0

        suffix loop

        start nums: [1,-1,0,0,0]
        p=1
        nums: [1,-1,0,0,1]
        
        """
        
        # prefix loop
        res = [1] * len(nums)
        p = 1

        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]

        # suffix loop
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
                
        return res

