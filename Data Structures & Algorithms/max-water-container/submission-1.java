class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;

        int maxArea = Integer.MIN_VALUE;

        while (l < r) {
            // Calculate area
            int height = Math.min(heights[l], heights[r]);
            int width = r - l;

            // Update max area
            maxArea = Math.max(width * height, maxArea);

            // Update pointers based on tower heights
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return maxArea;
    }
}
