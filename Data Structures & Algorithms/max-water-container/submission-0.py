class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area = length * width
        """

        l, r = 0, len(heights) - 1
        maxArea = float("-inf")

        while l < r:
            # update largest seen area
            length = min(heights[l], heights[r]) 
            width = r - l
            maxArea = max(maxArea, length * width)
        
            # move the pointer with the smallest heigh value
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxArea



        