class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        st=[]
        ans=[-1]*len(a)
        k=len(a)-1
        for i in range(len(a)-1,-1,-1):
            while st and a[i]>=a[st[-1]]:
                st.pop()
            if not st:
                ans[i]=0
            else:
                ans[i]=(st[-1]-k)
            st.append(i)
            k-=1
        return ans