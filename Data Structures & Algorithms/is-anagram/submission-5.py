class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = defaultdict(int), defaultdict(int)

        # count chars in s
        for c in s:
            s_count[c] += 1
        
        # count chars in t
        for c in t:
            t_count[c] += 1
        
        # compare if they have the same count
        return s_count == t_count