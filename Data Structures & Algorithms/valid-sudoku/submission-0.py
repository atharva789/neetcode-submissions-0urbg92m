import math

class Solution:
    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def get_grid_idx(self, row_idx, col_idx)->int:
        val = row_idx *3 + col_idx 
        return val 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board[0])
        col_hashset, row_hashset = {i: set() for i in range(size)}, {i: set() for i in range(size)}
        grid_sets = {i: set() for i in range(size)}
        for row_idx,row in enumerate(board):
            for i,val in enumerate(row):
                if val in row_hashset[row_idx] or val in col_hashset[i]:
                    print(f"\trow/col condition triggered!!\n\tDuplicate in row: {row_idx+1} or column: {i+1}. Duplicated value: {val}")
                    return False
                if val == ".":
                    val = 0
                row_hashset[row_idx].add(val)
                col_hashset[i].add(val)
                # identify grid: ceiling of row, col idx
                grid_row_idx, grid_col_idx = math.ceil((row_idx+1)/3)-1, math.ceil((i+1)/3) -1
                grid_idx = self.get_grid_idx(grid_row_idx, grid_col_idx)
                if int(val) in grid_sets[grid_idx]:
                    print(f"\tgrid_sum triggered!!")
                    return False
                if int(val) != 0:
                    grid_sets[grid_idx].add(int(val))
        return True