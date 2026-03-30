class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
          0 1 2 3 4 5
        [-1,0,2,4,6,8]
                l m r

        target = 4
        2 < 4, move 
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            # remove left half
            if nums[mid] < target:
                l = mid + 1
                
            # remove right half
            elif nums[mid] > target:
                r = mid - 1
            
            # target found
            else:
                return mid

        return -1