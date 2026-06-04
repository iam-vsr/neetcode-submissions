class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        f1 = Counter(s1)
        window = Counter(s2[:n1])

        if window == f1:
            return True

        for i in range(n1, n2):
            window[s2[i]] += 1        # add new char
            window[s2[i-n1]] -= 1     # remove old char
            if window[s2[i-n1]] == 0: # clean up zero counts
                del window[s2[i-n1]]
            if window == f1:
                return True

        return False

