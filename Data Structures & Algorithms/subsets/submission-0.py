class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def solve(arr,output):

            if len(arr)==0:
                ans.append(output)
                return
            
            solve(arr[1:],output)
            solve(arr[1:],output+[arr[0]])
        
        solve(nums,[])
        return ans