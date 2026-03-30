class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]
              ^  ^ 

                    i
        [-4,-1,-1,0,1,2]
            ^         ^

        i = -4
        4 = j + k

        i = -1
        1 = j + k (j=-1, k=2)
        1 = -1 + 2  => [-1,-1,2]

        i = -1
        1 = j + k (j=-1, k=2)
        1 = -1 + 2  => [-1,-1,2]
        
        ---

        i + j + k = 0
        -i = j + k
        
        """
        
        nums = sorted(nums)      # sorted(nums) uses extra space
        result = []

        # -i = j + k
        for i in range(len(nums)):
            # if i is positive, then impossible to find j+k
            if nums[i] > 0:
                break

            # prev value shouldn't be the same
            # we already computed i-1th index, dont compute again
            # EXAMPLE
            # [-5,-3,-3,-3,2,0,1]
            #      i  j        k
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # sum = i + j + k
            j, k = i+1, len(nums) - 1
            while j < k:
                # can also do -i = j + k, find target -i
                sum = nums[i] + nums[j] + nums[k]
                
                # increase sum, too low                
                if sum < 0:
                    j += 1
                
                # decrease sum, too high
                elif sum > 0:
                    k -= 1

                # sum == 0, found i,j,k
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    """
                    update j, so we dont have duplicate
                    e.g., move j until we reach 2
                    [-5,-3,-3, -3, 2....]
                         i  j->         k

                    update k so we dont have duplicate
                    e.g., move k until we reach 0
                    [............,0,1,1, 1]
                         i     j        <-k
                    """
                    j, k = j+1, k-1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return result


