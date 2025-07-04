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

# 3^6 boards (minus the completely illegal ones)
print(len(boards))




