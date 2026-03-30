class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        use 2 dicts to count # of chars in s and t
        
        check if both dicts are the same
        """
        
        s = s.strip()
        t = t.strip()

        # palindromes must have the same length
        if len(s) != len(t):
            return False

        # compare counts of characters
        c1 = {}
        c2 = {}

        # count chars in s
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            # count s chars
            if s_char in c1:
                c1[s_char] += 1
            else:
                c1[s_char] = 1
            
            # count t chars
            if t_char in c2:
                c2[t_char] += 1
            else:
                c2[t_char] = 1
        
        return c1 == c2
            



        