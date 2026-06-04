class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def nse(a):
            n=len(a)
            st=[]
            ans=[0]*n

            for i in range(n-1,-1,-1):

                while st and a[st[-1]]>=a[i]:
                    st.pop()
                if not st:
                    ans[i]=n
                else:
                    ans[i]=st[-1]
                st.append(i)
            return ans
        
        def pse(a):
            n=len(a)
            st=[]
            ans=[0]*n

            for i in range(n):

                while st and a[st[-1]]>=a[i]:
                    st.pop()
                if not st:
                    ans[i]=-1
                else:
                    ans[i]=st[-1]
                st.append(i)
            return ans
        
        a1, a2 = nse(heights), pse(heights)
        maxi=0
        for i in range(len(heights)):
            maxi= max(maxi, (a1[i]-a2[i]-1)*heights[i])
        return maxi
    
                    





        