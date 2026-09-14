class TrieNode:
    def __init__(self):
        self.children={}
        self.word_end=False
    
    def addWord(self, word):
        node=self
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.word_end=True

class Solution:
   
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
 
        for word in words:
            root.addWord(word)
        
        rows=len(board)
        cols=len(board[0])
        visit=set()
        ans=set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or r>rows-1 or c>cols-1 
            or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))

            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.word_end:
                ans.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(ans)
        