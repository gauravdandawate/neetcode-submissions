class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s_chars = list(s)
    #     t_chars = list(t)
    #     return sorted(s_chars) == sorted(t_chars)


    ## create a dict as ( letter, count(letter)) and compare
    #this will restrict the dict to max 26 - saving on space complexity
    def isAnagram(self, s: str, t: str) -> bool:

        sdict = {}
        tdict = {}

        for c in s:
            # dict.get(c,0)- it will get current value if present , else return 0 as default
            sdict[c] = sdict.get(c,0) + 1
        for c in t:
            tdict[c] = tdict.get(c,0) + 1

        return sdict == tdict


