class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        f1=Counter(s)
        f2=Counter(t)
        return f1==f2