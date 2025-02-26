from collections import deque
import numpy as np

boards = []
final_boards = []


for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        pos_boards = np.array([[i, j, k],
                                               [l, m, n]])
                        num_1 = np.count_nonzero(pos_boards == 1)
                        num_2 = np.count_nonzero(pos_boards == 2)
                        if num_1 <= 3 and num_2 <= 2 and (num_1 == num_2 or num_1 == num_2 + 1):
                            boards.append(pos_boards)


def bfs_board(board):
    queue = deque()

    for i in range(2):
        for j in range(3):
            explored = []
            queue.appendleft(board[i, j])
            while len(queue) > 0:
                v = queue.pop()
                if v == 0:
                    return True
                explored.append((i, j))
                if v == 1:
                    if i == 0 and (not explored.__contains__((i+1, j))) and board[i+1, j] != 2:
                        explored.append((i+1, j))
                        queue.appendleft(board[i+1, j])
                    if i == 1 and (not explored.__contains__((i-1, j))) and board[i-1, j] != 2:
                        explored.append((i-1, j))
                        queue.appendleft(board[i-1, j])
                    if j != 2 and (not explored.__contains__((i, j+1))) and board[i, j+1] != 2:
                        explored.append((i, j+1))
                        queue.appendleft(board[i, j + 1])
                    if j != 0 and (not explored.__contains__((i, j-1))) and board[i, j-1] != 2:
                        explored.append((i, j-1))
                        queue.appendleft(board[i, j - 1])
                        
                if v == 2:
                    if i == 0 and (not explored.__contains__((i+1, j))) and board[i+1, j] != 1:
                        explored.append((i+1, j))
                        queue.appendleft(board[i+1, j])
                    if i == 1 and (not explored.__contains__((i-1, j))) and board[i-1, j] != 1:
                        explored.append((i-1, j))
                        queue.appendleft(board[i-1, j])
                    if j != 2 and (not explored.__contains__((i, j+1))) and board[i, j+1] != 1:
                        explored.append((i, j+1))
                        queue.appendleft(board[i, j + 1])
                    if j != 0 and (not explored.__contains__((i, j-1))) and board[i, j-1] != 1:
                        explored.append((i, j-1))
                        queue.appendleft(board[i, j - 1])
                if len(queue) == 0:
                    return False


for i in range(len(boards)):
    if not bfs_board(boards[i]):
        final_boards.append(boards[i])


for i in final_boards:
    print(i)
    print()
print(len(final_boards))
