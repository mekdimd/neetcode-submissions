class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        
        while l < r:
            mid = (l + r) // 2
            
            # left half not present
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # mid <= nums, regular sorted
            else:
                r = mid

        # l = r, return min
        return nums[l]
