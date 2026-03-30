class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = defaultdict(int), defaultdict(int)

        # count chars in s and t
        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        
        # compare if they have the same count
        return s_count == t_count