def isValidSudoku(board):
     rows = [set() for _ in range(9)]
     cols = [set() for _ in range(9)]
     grid = [set() for _ in range(9)]


     for row in range(9): 
          for col in range(9):
               num = board[row][col]
               if num == ".": 
                    continue
               grid_ind = (row // 3) * 3 + col // 3 
               if num in rows[row] or num in cols[col] or num in grid[grid_ind]: 
                    return False 
               rows[row].add(num)
               cols[col].add(num)
               grid[grid_ind].add(num)
     return True
               
print(isValidSudoku([

 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 
 ]))