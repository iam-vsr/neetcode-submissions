from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n=len(hand)
        if n%gs!=0:
            return False
        
        freq=Counter(hand)
        hand.sort()

        for num in hand:
            if freq[num]:
                for i in range(num,num+gs):
                    if not freq[i]:
                        return False
                    freq[i]-=1
        return True
            

