class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root   
        
        for c in word:
            # create new TrieNode node if needed
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        # mark as end of word
        curr.is_end = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                # wild card, can be any child
                if c == '.':
                    # check all children
                    for child in curr.children.values():
                        # one match found
                        if dfs(i+1, child):
                            return True

                    # no matches found in children
                    return False

                # c is regular char. proceed as normal
                else:
                    
                    # cant find next char in word
                    if c not in curr.children:
                        return False
                    
                    curr = curr.children[c]

            # last char must be end of the word
            return curr.is_end
        
        return dfs(0, self.root)
        
