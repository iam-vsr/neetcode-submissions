class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=0
        ans=[]
        q=deque()

        while r<len(nums):
        # 1. Maintain decreasing order: pop elements smaller than the incoming nums[r]
            while q and nums[q[-1]]<nums[r]:
                q.pop()
         # 2. Append current element's index
            q.append(r)
            
        # 3. Evict elements that fell outside the left window boundary
            if l>q[0]:
                q.popleft()
        # 4. Once the first window of size k is formed, append the max to ans
            if r+1>=k:
                ans.append(nums[q[0]])
                l+=1
            r+=1
        return ans
