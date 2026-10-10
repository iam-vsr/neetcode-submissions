class Solution:
    def ladderLength(self, beginword: str, endword: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endword not in wordset:
            return 0
        
        q=deque([(beginword,1)])

        while q:
            word,step=q.popleft()
            if word==endword:
                return step
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]

                    if new_word in wordset:
                        wordset.remove(new_word)
                        q.append((new_word,step+1))
        
        return 0