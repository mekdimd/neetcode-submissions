class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        l == mid
        return mid

        LEFT HALF SORTED
        
        l < mid
                        t 
        nums = [4,5,6,7,0,1,2]
                l     m     r

        nums = [1,2]
                lm r

        mid < right
                          t
        nums = [7,0,1,2,4,5,6]
                l     m     r     

        ----

        RIGHT HALF SORTED
        
        l > mid           
                          t
        nums = [7,0,1,2,4,5,6]
                l     m     r

                    t
        nums = [5,1,3]
                l m r

                t
        nums = [1,3,5]
                l m r
        """

        l, r = 0, len(nums) - 1

        while l <= r:            
            mid = (l + r) // 2

            # target found
            if nums[mid] == target:
                return mid

            # left half is sorted
            elif nums[l] <= nums[mid]:
                # target outside sorted half
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right half is sorted
            else:
                # target outside sorted half
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        # target not found
        return -1