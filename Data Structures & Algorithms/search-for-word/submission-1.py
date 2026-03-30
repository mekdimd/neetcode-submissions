class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j = 0,0

        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, j, word_idx):
            # word has been found
            if word_idx == len(word):
                return True
            
            # invalid index
            if i < 0 or i >= rows:
                return False
            if j < 0 or j >= cols:
                return False
            
            # invalid char
            if board[i][j] != word[word_idx]:
                return False

            # Mark current cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # check if curr board element is correct
            if word[word_idx] == board[i][j]:
                word_idx += 1
                return True
            
            # Check neighbours
            found = (
                dfs(i+1, j, word_idx+1) or
                dfs(i-1, j, word_idx+1) or
                dfs(i, j+1, word_idx+1) or
                dfs(i, j-1, word_idx+1)
            )

            # backtrack
            # restore old value of cell
            board[i][j] = temp

            return found

        # Try every cell as a starting point
        # Not just (0,0)
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
