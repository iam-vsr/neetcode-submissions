class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        ans=[]

        for i in range(len(temp)-1,-1,-1):
            while stack and temp[i]>=stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][1]-i)
            stack.append((temp[i],i))
        
        return ans[::-1]



