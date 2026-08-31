class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has={}

        for st in strs:
            alph=[0]*26
            for ch in st:
                alph[ord(ch)-ord('a')]+=1
            
            key = tuple(alph)
            if key in has:
                has[key].append(st)
            else:
                has[key]=[st]
        
        return list(has.values())

