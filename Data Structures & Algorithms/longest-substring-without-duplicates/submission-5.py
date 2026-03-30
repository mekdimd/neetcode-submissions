class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case: 0/1
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 0
        seen = set()
        max_len = 0
        
        while r < len(s):
            # duplicate char entered window, move window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # increase window
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len