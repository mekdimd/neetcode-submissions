class TrieNode:
    def __init__(self):
        self.children = {}  # hashmap of children - O(26)
        self.end_word = False
    

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            # create new char if it doesnt exist
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            # traverse down tree
            curr = curr.children[c]
        
        # mark last char as end
        curr.end_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            # char must be present
            if c not in curr.children:
                return False
            
            # traverse
            curr = curr.children[c]
        
        # word must be ending
        return bool(curr.end_word)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            # char must be present
            if c not in curr.children:
                return False
            
            # traverse
            curr = curr.children[c]
        
        # prefix exists, return true
        return True
        