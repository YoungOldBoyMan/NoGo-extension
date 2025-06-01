import matplotlib.pyplot as plt
import numpy as np


def draw_board(board):
    size = board.shape[0]
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.add_patch(plt.Rectangle((0, 0), size-1, size-1, color='#DEB887', zorder=0))

    move_number = 1
    
    # Draw grid
    for i in range(size):
        ax.plot([0, size-1], [i, i], color='black')  # horizontal
        ax.plot([i, i], [0, size-1], color='black')  # vertical

    for i in range(size):
        for j in range(size):
            if board[i, j] == 1:
                ax.add_patch(plt.Circle((j, size-1-i), 0.3, color='black', zorder=2))
                ax.text(j, size-1-i, str(move_number), 
                        ha='center', va='center',
                        color='white', fontsize=12, fontweight='bold', zorder=3)
                move_number += 1
            elif board[i, j] == 2:
                ax.add_patch(plt.Circle((j, size-1-i), 0.3,
                             color='#F6F4EB', ec='black', zorder=2))
                ax.text(j, size-1-i, str(move_number),
                        ha='center', va='center',
                        color='black', fontsize=12, fontweight='bold', zorder=3)
                move_number += 1

            
    # Set ticks
    ax.set_xticks(range(size))
    ax.set_yticks(range(size))
    ax.set_xticklabels(['1', '2', '3'])
    ax.set_yticklabels([str(i+1) for i in reversed(range(size))][::-1])

    ax.set_aspect('equal')
    ax.tick_params(axis='both', which='both', length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.show()


# make example board
example_board = np.array([
    [0, 0, 1],
    [2, 0, 0],
    [1, 2, 0],
])

draw_board(example_board)
