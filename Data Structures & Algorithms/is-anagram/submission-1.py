class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Sort arrays
        s_sorted = sorted(s.strip())
        t_sorted = sorted(t.strip())

        # Check if each character matches
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False

        return True
        