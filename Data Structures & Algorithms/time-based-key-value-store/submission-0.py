class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timestamps=self.store[key]
        l=0
        r=len(timestamps)-1
        res=""
        while l<=r:
            m=r-(r-l)//2
            if timestamps[m][1]<=timestamp:
                res=timestamps[m][0]
                l=m+1
            else:
                r=m-1
        
        return res
        
