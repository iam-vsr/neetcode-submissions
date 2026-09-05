class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def backtrack(i,curr,total):
            if total==target:
                res.append(curr[:])
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j-1]==candidates[j]:
                    continue
                if total+candidates[j]>target:
                    break

                curr.append(candidates[j])
                backtrack(j+1,curr,total+candidates[j])
                curr.pop()

        backtrack(0,[],0)
        return res
                
