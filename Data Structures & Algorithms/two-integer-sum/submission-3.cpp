class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> lookup;

        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // number found
            if (lookup.contains(nums[i])) {
                return {lookup[nums[i]], i};
            }

            // keep counting
            lookup[diff] = i;
        }

        return {};
    }
};
