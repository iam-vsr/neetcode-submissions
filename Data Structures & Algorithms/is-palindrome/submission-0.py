class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        s=s.lower()
        for i in range(len(s)):
            if (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                a.append(s[i])
        n=len(a)
        for i in range(n//2):
            if a[i]!=a[n-i-1]:
                return False
        return True