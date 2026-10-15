class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        
        curr=0
        start_idx=0
        for i in range(len(gas)):
            curr+=(gas[i]-cost[i])

            if curr<0:
                start_idx=i+1
                curr=0
        
        return start_idx