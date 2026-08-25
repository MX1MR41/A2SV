class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # approach works by finding the next letter of the word on either 
        # four directions of a given coordinate in a recursive manner
        m = len(board)
        n = len(board[0])

        # params are the board i
        def search(r, c, ind):
            nonlocal board, word, m, n
            if ind == len(word):
                return True

            # base cases; boundary reaching or exploring an already seen letter
            if r < 0 or c < 0 or r == m or c == n or board[r][c] != word[ind] or board[r][c] == 'seen':
                return False

            # we store the letter we currently are at and mark it as seen
            # so we don't double count it in case one of our recursive calls 
            # tries to explore it
            temp = board[r][c]
            board[r][c] = 'seen'

            # we search in the four directions for the next letter of the word
            # and if one of them found the rest of the word, we return it
            up = search(r - 1, c, ind + 1) # search up
            down = search(r + 1, c, ind + 1) # search down
            right = search(r, c + 1, ind + 1) # search right
            left = search(r, c - 1, ind + 1) # search 

            # reassign the value we have marked as seen back to its original value
            board[r][c] = temp

            return up or down or right or left

        for i in range(m):
            for j in range(n):
                # first letter
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True

        return False

        


        