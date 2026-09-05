class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        visited=[False]*len(nums)

        def dfs(curr):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    visited[i]=False
        
        dfs([])
        return ans
