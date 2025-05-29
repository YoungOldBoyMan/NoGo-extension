from collections import deque
import numpy as np

BOARD_X = 1
BOARD_Y = 12

black_win_boards = []
white_win_boards = []
final_boards = []

var_names = ["i" + str(i) for i in range(BOARD_X*BOARD_Y)]
out_str = ""

loop_vars = []
board_code = ""
cell_index = 0


for var in var_names:
    out_str += f"for {var} in range(3):\n"
    out_str += "    " * (len(loop_vars) + 1) 
    loop_vars.append(var)

rows = []
for row in range(BOARD_X):
    row_vars = var_names[row * BOARD_Y:(row + 1) * BOARD_Y]
    rows.append("[" + ", ".join(row_vars) + "]")
board_assignment = f"pos_boards = np.array([{', '.join(rows)}])\n"

board_logic = """\
num_1 = np.count_nonzero(pos_boards == 1)
num_2 = np.count_nonzero(pos_boards == 2)
if num_1 == num_2:
    black_win_boards.append(pos_boards)
elif num_1 == num_2 + 1:
    white_win_boards.append(pos_boards)
"""

full_code = out_str + "\n" + "    " * (BOARD_X*BOARD_Y) + board_assignment
full_code += "    " * (BOARD_Y * BOARD_X) + board_logic.replace("\n", "\n" + "    " * (BOARD_X * BOARD_Y))

print(full_code)

for i0 in range(3):
    for i1 in range(3):
        for i2 in range(3):
            for i3 in range(3):
                for i4 in range(3):
                    for i5 in range(3):
                        for i6 in range(3):
                            for i7 in range(3):
                                for i8 in range(3):
                                    for i9 in range(3):
                                        for i10 in range(3):
                                            for i11 in range(3):

                                                pos_boards = np.array([[i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11]])
                                                num_1 = np.count_nonzero(pos_boards == 1)
                                                num_2 = np.count_nonzero(pos_boards == 2)
                                                if num_1 == num_2:
                                                    black_win_boards.append(pos_boards)
                                                elif num_1 == num_2 + 1:
                                                    white_win_boards.append(pos_boards)

def bfs_board(board):

    for i in range(BOARD_X):
        for j in range(BOARD_Y):
            queue = deque()
            point_queue = deque()
            explored = []
            queue.appendleft(board[i, j])
            point_queue.appendleft((i, j))
            while len(queue) > 0:
                v = queue.pop()
                point = point_queue.pop()
                new_i, new_j = point
                if v == 0:
                    break
                explored.append((new_i, new_j))
                # print(explored)
                if v == 1:
                    if new_i != (BOARD_X-1) and (not explored.__contains__((new_i+1, new_j))) and board[new_i+1, new_j] != 2:
                        explored.append((new_i+1, new_j))
                        queue.appendleft(board[new_i+1, new_j])
                        point_queue.appendleft((new_i+1, new_j))
                    if new_i != 0 and (not explored.__contains__((new_i-1, new_j))) and board[new_i-1, new_j] != 2:
                        explored.append((new_i-1, new_j))
                        queue.appendleft(board[new_i-1, new_j])
                        point_queue.appendleft((new_i-1, new_j))
                    if new_j != (BOARD_Y-1) and (not explored.__contains__((new_i, new_j+1))) and board[new_i, new_j+1] != 2:
                        explored.append((new_i, new_j+1))
                        queue.appendleft(board[new_i, new_j + 1])
                        point_queue.appendleft((new_i, new_j+1))
                    if new_j != 0 and (not explored.__contains__((new_i, new_j-1))) and board[new_i, new_j-1] != 2:
                        explored.append((new_i, new_j-1))
                        queue.appendleft(board[new_i, new_j - 1])
                        point_queue.appendleft((new_i, new_j-1))

                if v == 2:
                    if new_i != (BOARD_X-1) and (not explored.__contains__((new_i+1, new_j))) and board[new_i+1, new_j] != 1:
                        explored.append((new_i+1, new_j))
                        queue.appendleft(board[new_i+1, new_j])
                        point_queue.appendleft((new_i+1, new_j))
                    if new_i != 0 and (not explored.__contains__((new_i-1, new_j))) and board[new_i-1, new_j] != 1:
                        explored.append((new_i-1, new_j))
                        queue.appendleft(board[new_i-1, new_j])
                        point_queue.appendleft((new_i-1, new_j))
                    if new_j != (BOARD_Y-1) and (not explored.__contains__((new_i, new_j+1))) and board[new_i, new_j+1] != 1:
                        explored.append((new_i, new_j+1))
                        queue.appendleft(board[new_i, new_j + 1])
                        point_queue.appendleft((new_i, new_j+1))
                    if new_j != 0 and (not explored.__contains__((new_i, new_j-1))) and board[new_i, new_j-1] != 1:
                        explored.append((new_i, new_j-1))
                        queue.appendleft(board[new_i, new_j - 1])
                        point_queue.appendleft((new_i, new_j-1))
                if len(queue) == 0:
                    return False
    return True

# if not bfs_board(boards[-2], BOARD_X, BOARD_Y):
#     final_boards.append(boards[-2])
# print(final_boards)

# for i in range(len(black_win_boards)):
#     if not bfs_board(black_win_boards[i]):
#         final_boards.append(black_win_boards[i])

for i in range(len(black_win_boards)):
    if not bfs_board(black_win_boards[i]):
        final_boards.append(black_win_boards[i])

print(len(final_boards))

