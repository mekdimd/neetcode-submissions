class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      def binarySearch(arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
          mid = (l+r)//2
          if arr[mid] == target:
            return True
          elif arr[mid] < target:
            l = mid + 1
          else:
            r = mid - 1

        return False

      # Run binary search for each row of the matrix
      # O(N) * logM 
      for arr in matrix:
        lower, upper = arr[0], arr[-1]
        
        # check if value is in range
        if lower <= target <= upper:
          return binarySearch(arr, target)
        
        # if binarySearch(arr, target):
        #   return True
      
      return False