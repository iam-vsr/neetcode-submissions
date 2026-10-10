class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words: 
            for c in w:
                adj[c] = set()
        indegree={ch:0 for ch in adj}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            if len(w1)>len(w2) and w1[:len(w2)]==w2:
                return ""
            
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        for u in adj:
            for v in adj[u]:
                indegree[v]+=1
        
        q=deque()
        for ch in indegree:
            if indegree[ch]==0:
                q.append(ch)
        
        order=[]
        while q:
            ch=q.popleft()
            order.append(ch)

            for ne in adj[ch]:
                indegree[ne]-=1

                if indegree[ne]==0:
                    q.append(ne)
        
        if len(order)!=len(adj):
            return ""
        
        return "".join(order)
        
        