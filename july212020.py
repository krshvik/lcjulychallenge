class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == []:
            return False
        
        lenb = len(board)
        i = 0 
        while i < lenb:
            lenc = len(board[i])
            j = 0 
            while j < lenc:
                if board[i][j] == word[:1]:
                    if self.findword(board,i,j,word):
                        return True
                j = j + 1 
            i = i + 1
        return False 
    
    def findword(self,board,crow,ccol,word):
        
        if word == board[crow][ccol]:
            return True
        
        if word[:1] != board[crow][ccol]:
            return False
        
        if crow < len(board)-1:
            board[crow][ccol] = '!'
            if self.findword(board,crow+1,ccol,word[1:]):
                return True
            board[crow][ccol] = word[:1]
        
        if crow > 0:
            board[crow][ccol] = '!'
            if self.findword(board,crow-1,ccol,word[1:]):
                return True
            board[crow][ccol] = word[:1]
            
        if ccol > 0:
            board[crow][ccol] = '!'
            if self.findword(board,crow,ccol-1,word[1:]):
                return True
            board[crow][ccol] = word[:1]
        
        if ccol < len(board[crow]) - 1:
            board[crow][ccol] = '!'
            if self.findword(board,crow,ccol+1,word[1:]):
                return True
            board[crow][ccol] = word[:1]
        
        return False 