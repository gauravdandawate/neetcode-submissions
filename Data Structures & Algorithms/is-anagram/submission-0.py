class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars=list(s)
        t_chars=list(t)
        return sorted(s_chars) == sorted(t_chars)