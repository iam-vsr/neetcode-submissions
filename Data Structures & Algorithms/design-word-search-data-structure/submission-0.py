class TrieNode():

    def __init__(self):
        self.children={}
        self.word_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.word_end=True

    def search(self, word: str) -> bool:
        def dfs(i, node): #recursive as multiple ways
            if i==len(word):
                return node.word_end
            
            ch=word[i]

            if ch!='.': #normal case
                if ch not in node.children:
                    return False
                return dfs(i+1, node.children[ch])
            
            else:
                for child in node.children.values():
                    if dfs(i+1, child): #try for every child 
                        return True
                return False
        
        return dfs(0,self.root)


