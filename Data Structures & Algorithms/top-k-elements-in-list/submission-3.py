class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = defaultdict(int)

        for num in nums:
            has[num]+=1
        
        buckets = [[] for _ in range(len(nums)+1)]
        
        for key, value in has.items():
            buckets[value].append(key)
        

        res=[]
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res
        
        return res
        