class Solution {
    public int[] twoSum(int[] nums, int target) {
        /**
        nums = [3,5,6,4], target = 7
        { i=3, nums[i]=4
            4: 0
            2: 1
            1: 2
        }

        */
        
        Map<Integer, Integer> count = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            // contained in hashmap
            if (count.containsKey(nums[i])) {
                return new int[]{count.get(nums[i]), i};
            }

            count.put(diff, i);
        }

        return new int[]{};
    }
}
