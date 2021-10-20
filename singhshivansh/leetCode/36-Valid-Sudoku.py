# Author: @Iresharma
# https://leetcode.com/problems/36-Valid-Sudoku/

"""
Runtime: 88 ms, faster than 95.88% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.2 MB, less than 87.74% of Python3 online submissions for Valid Sudoku.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, block = set(), set(), set()
        
        for i in  range(9):
            for j in range(9):
                if board[i][j] != ".":
                    r_key = (i, board[i][j])
                    c_key = (j, board[i][j])
                    b_key = (i // 3, j // 3, board[i][j])
                    
                    if (r_key in row) or (c_key in col) or (b_key in block):
                        return False
                    
                    row.add(r_key)
                    col.add(c_key)
                    block.add(b_key)
        return True