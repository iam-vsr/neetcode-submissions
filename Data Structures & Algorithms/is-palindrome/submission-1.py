class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        arr=[]
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                arr.append(ch)
        
        return arr==arr[::-1]