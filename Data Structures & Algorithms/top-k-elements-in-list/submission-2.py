class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = defaultdict(int)

        for num in nums:
            has[num]+=1
        
        arr=[]
        for key, value in has.items():
            arr.append((value,key))
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        
        return res
        