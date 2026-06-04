class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in f.items():
            bucket[count].append(num)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans

