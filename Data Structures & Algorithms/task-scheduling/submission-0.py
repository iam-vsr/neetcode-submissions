class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_list=list(Counter(tasks).values())
        max_freq=max(freq_list)
        max_freq_count=0
        for i in freq_list:
            if i==max_freq:
                max_freq_count+=1
        
        time=(max_freq-1)*(n+1)+max_freq_count
        return max(len(tasks),time)