from collections import defaultdict
from typing import List

board =[[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

#print(board)
def row_index(i,j):
    return (i, j)

def col_index(i,j):
    return (j, i)

def box_index(i, j):
    Mj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    Mi = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    return (Mi[i] * 3 + Mi[j], Mj[i]*3 + Mj[j])

def _board(index):
    i,j = index
    return board[i][j]

def check_consistency(index,check_map):
     val = int(_board(index)) if(_board(index)).isnumeric() else -1
     if((val>0)):
         if check_map[val]:
             print(index,val)
             return 0
         else:
            return val


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # check_map = dict.fromkeys(val,1)
    #     for i in range(9):
    #         check_map_row =[0]*len(board)
    #         check_map_column = [0]*len(board[0])
    #         check_map_box = [[[0]  for _ in range(len(board[0]))] for _ in range(len(board))]
    #         for j in range(9):
    #             column_index = col_index(i,j)
    #             column_consitency  = check_consistency(column_index,check_map_column)
    #             if(column_consitency):check_map_column[column_consitency]=1
    #             else: return False

    #             r_index = row_index(i,j)
    #             row_consitency  = check_consistency(r_index,check_map_row)
    #             if(row_consitency):check_map_row[row_consitency]=1
    #             else: return False

    #             b_index = box_index(i,j)
    #             box_consitency  = check_consistency(box_index,check_map_box)
    #             if(box_consitency):check_map_box[box_consitency]=1
    #             else: return False

    #             column_index = col_index(i,j)
    #             column_consitency  = check_consistency(column_index,check_map_column)
    #             if(column_consitency):check_map_column[column_consitency]=1


    #             val_row = int(_board(row_index(i,j))) if(_board(row_index(i,j))).isnumeric() else -1
    #             val_column = int(_board(col_index(i,j))) if(_board(col_index(i,j))).isnumeric() else -1
    #             val_box =  int(_board(box_index(i,j))) if(_board(box_index(i,j))).isnumeric() else -1

    #             if((val_row>0)):
    #                 if check_map_row[val_row]:
    #                     print("row",i,"column",j,val_row)
    #                     return False
    #                 else:
    #                     check_map_row[val_row]=1

    #             if(val_column>0):
    #                if check_map_column[val_column]:
    #                    print("row",i,"column",j,val_row)
    #                    return False
    #                else:
    #                    check_map_row[val_column]=1

    #             if(val_box>0):
    #                if check_map_column[val_column]:
    #                    print("row",i,"column",j,val_row)
    #                    return False
    #                else:
    #                    check_map_row[val_column]=1


    #         print()

    #     # for k in range(0,9,3):
    #     #     check_map_row = dict.fromkeys([x for x in range(1,10)],1)
    #     #     check_map_column = dict.fromkeys([x for x in range(1,10)],1)
    #     #     for i in range(k,k+3):
    #     #         for j in range(k,k+3):

    #     #             val_row = int(board[i][j]) if board[i][j].isnumeric() else -1
    #     #             val_column = int(board[j][i]) if board[j][i].isnumeric() else -1
    #     #             print(i,j,val_row,val_column)
    #     #             board[i][j]='a'
    #     #             if((val_row>0)):
    #     #                 if check_map_row[val_row]:
    #     #                     check_map_row[val_row]=0
    #     #                 else:
    #     #                     print("row",i,"column",j,val_row)
    #     #                     return False
    #     #             if(val_column>0):
    #     #                 if check_map_column[val_column]:
    #     #                     check_map_column[val_column]=0
    #     #                 else:
    #     #                     print("row",i,"column",j,val_column)
    #     #                     return False
    #     for i in range(9):
    #         for j in range(9):
    #             print(board[i][j],end=' ')
    #         print()

    #     return True


check_map_box = [[[0]  for _ in range(len(board[0]))] for _ in range(len(board))]

eval = Solution()
out1  = eval.isValidSudoku(board)
print(out1)
