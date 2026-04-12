class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        Time: O(N^2)
            O(N) to check each i as center of palindrome
            for each i, check palindrome - O(N)
        
        Space: O(1)
            or O(n) with string copy
            can replace with indices, but code is messier
        """
        
        if not s: 
            return ""

        res = ''
        
        def expand(l, r):
            # expand l,r outwards until no longer palindrome
            # while idx in bounds + substr is palindrome
            # [a,a,b,b,a,a]
            #    ← l r →
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        # check all n chars for starting point
        for i in range(len(s)):
            # Case 1: odd length
            # e.g. aba
            #       i
            len_odd = expand(i, i)

            # Case 2: even length 
            # (e.g. abba)
            #        ^^
            len_even = expand(i, i+1)

            # update max length 
            res = max(len_odd, len_even, res, key=len)


        return res