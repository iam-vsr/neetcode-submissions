class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nsei=[]
        psei=[]

        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                nsei.append(n)
            else:
                nsei.append(stack[-1])
            stack.append(i)
        nsei=nsei[::-1]

        stack=[]
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                psei.append(-1)
            else:
                psei.append(stack[-1])
            stack.append(i)
        
        max_area=0
        for i in range(len(heights)):
            max_area=max(max_area, (nsei[i]-psei[i]-1)*heights[i])
        return max_area

        


        