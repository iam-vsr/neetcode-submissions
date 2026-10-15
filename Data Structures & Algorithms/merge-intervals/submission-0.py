class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        n=len(arr)
        arr.sort()
        ans=[]
        l=arr[0][0]
        r=arr[0][1]

        for i in range(1,n):
            if r>=arr[i][0]:
                l=min(arr[i][0],l)
                r=max(arr[i][1],r)
            else:
                ans.append([l,r])
                l=arr[i][0]
                r=arr[i][1]
        
        ans.append([l,r])
        return ans