# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         has1=defaultdict(int)
#         for ch in s1:
#             has1[ch]+=1
        
#         l=0
#         r=len(s1)-1
#         n=len(s2)

#         while r<n:
#             has2=defaultdict(int)
#             for i in range(l,r+1):
#                 has2[s2[i]]+=1
            
#             if has2==has1:
#                 return True
            
#             else:
#                 l+=1
#                 r+=1
        
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        has1 = defaultdict(int)
        has2 = defaultdict(int)
        
        # Build initial frequency maps for length n1
        for i in range(n1):
            has1[s1[i]] += 1
            has2[s2[i]] += 1
            
        if has1 == has2:
            return True
            
        # Slide the window across s2
        for r in range(n1, n2):
            l = r - n1
            
            # Add incoming character
            has2[s2[r]] += 1
            
            # Evict outgoing character
            has2[s2[l]] -= 1
            if has2[s2[l]] == 0: #clean up zero counts
                del has2[s2[l]]
                
            # Dictionary comparison takes O(26) = O(1)
            if has1 == has2:
                return True
                
        return False
            

