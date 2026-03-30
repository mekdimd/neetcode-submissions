class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AABBBCBBBBBBBBBB (k=1)
        
        ZZBVC BBYBCBB YYVBY, k=2
              l     r       
        replacements = 14 - 7 = 7 > k=2
        replacements = 7-5 = 2
        
        middle C -> B

        {
            B: 7-2 = 5
            Y: 4
            Z: 2
            V: 2
            C: 1
        }
        
        
        AAABABB, k=1, 8 chars
        l   r
        # replacments = (r-l+1) - count(A) = 5-4=1
        {
            A: 4
            B: 3
        }

        need 4 replacement

        O(N * 26)
        O(26) space
        
        """
        count = defaultdict(int)
        longest = 0
        
        l = 0
        for r in range(len(s)):
            # update count of curr char
            count[s[r]] += 1

            # update max length
            # window length: (r - l + 1) 
            # maxChar count: max(count.values())
            # if window is invalid, shrink window until it is valid
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1    # decrement count
                l += 1              # shrink window
            
            # window is valid, update longest
            longest = max(longest, r - l + 1)
        return longest

