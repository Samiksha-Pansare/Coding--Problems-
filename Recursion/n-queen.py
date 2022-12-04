class Solution:
    def solveNQueens(self, n):
        #  function issafe
        def is_safe(row,col,board,n):
            # Check Upper Diagonal
            duprow=row
            dupcol=col

            while(row>=0 and col>=0):
                if (board[row][col] == "Q"):
                    return False
                row=row-1
                col=col-1
            row = duprow
            col = dupcol
            while (col>=0):
                if board[row][col]=="Q":
                    return False
                col=col-1
            row = duprow
            col = dupcol
            while(row<n and col>=0):
                if (board[row][col]=="Q"):
                    return False
                row = row + 1
                col = col - 1
            return True
        # function solve
        def solve(col,board,ans,n):
            if col==n:
                ans.append(board[:])
                # print("Ans: ",ans)
                return
            for row in range(0,n):
                if(is_safe(row,col,board,n)):
                    l=list(board[row])
                    # print(l,type(l))
                    l[col]="Q"
                    board[row]="".join(l)
                    solve(col+1,board,ans,n)
                    temp = list(board[row])
                    temp[col]="." 
                    board[row]="".join(temp)           
        s=[]
        for i in range(0,n):
            s.append(".")
        board=[]
        for i in range(0,n):
            board.append(s)
        # print("Board: ",board)
        ans=[]
        solve(0,board,ans,n)
        return ans[0]
        # One Board has been Created
    
# name="SAM"
# name[0]="p"
# print(name)      
sol = Solution()
print(sol.solveNQueens(4))