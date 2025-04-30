from collections import deque
import numpy as np

whiteboards = []
blackboards = []
final_boards = []

# test comment
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        for o in range(3):
                            for p in range(3):
                                for q in range(3):
                                    pos_boards = np.array([[i, j, k],
                                                            [l, m, n], 
                                                            [o, p, q]])
                                    num_1 = np.count_nonzero(pos_boards == 1)
                                    num_2 = np.count_nonzero(pos_boards == 2)
                                    if (num_1==num_2):
                                        whiteboards.append(pos_boards)
                                    if  (num_1==num_2+1):
                                        blackboards.append(pos_boards)


def bfs_board(board):

    for i in range(3):
        for j in range(3):
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
                    if new_i != 2 and (not explored.__contains__((new_i+1, new_j))) and board[new_i+1, new_j] != 2:
                        explored.append((new_i+1, new_j))
                        queue.appendleft(board[new_i+1, new_j])
                        point_queue.appendleft((new_i+1, new_j))
                    if new_i != 0 and (not explored.__contains__((new_i-1, new_j))) and board[new_i-1, new_j] != 2:
                        explored.append((new_i-1, new_j))
                        queue.appendleft(board[new_i-1, new_j])
                        point_queue.appendleft((new_i-1, new_j))
                    if new_j != 2 and (not explored.__contains__((new_i, new_j+1))) and board[new_i, new_j+1] != 2:
                        explored.append((new_i, new_j+1))
                        queue.appendleft(board[new_i, new_j + 1])
                        point_queue.appendleft((new_i, new_j+1))
                    if new_j != 0 and (not explored.__contains__((new_i, new_j-1))) and board[new_i, new_j-1] != 2:
                        explored.append((new_i, new_j-1))
                        queue.appendleft(board[new_i, new_j - 1])
                        point_queue.appendleft((new_i, new_j-1))

                if v == 2:
                    if new_i != 2 and (not explored.__contains__((new_i+1, new_j))) and board[new_i+1, new_j] != 1:
                        explored.append((new_i+1, new_j))
                        queue.appendleft(board[new_i+1, new_j])
                        point_queue.appendleft((new_i+1, new_j))
                    if new_i != 0 and (not explored.__contains__((new_i-1, new_j))) and board[new_i-1, new_j] != 1:
                        explored.append((new_i-1, new_j))
                        queue.appendleft(board[new_i-1, new_j])
                        point_queue.appendleft((new_i-1, new_j))
                    if new_j != 2 and (not explored.__contains__((new_i, new_j+1))) and board[new_i, new_j+1] != 1:
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

# if not bfs_board(boards[-2]):
#     final_boards.append(boards[-2])
# print(final_boards)


for i in range(len(whiteboards)):
    if not bfs_board(whiteboards[i]):
        final_boards.append(whiteboards[i])


for i in final_boards:
    print(i)
    print()
print(final_boards[0])
