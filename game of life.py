import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def life (grid, generations):
    def roll_matrix(x, y):
        return np.roll(np.roll(grid, y, axis = 0), x, axis = 1)
    for _ in range (generations):
        neighbours = roll_matrix(1, 0) + roll_matrix(0, 1) + roll_matrix(-1, 0) + roll_matrix(0, -1) + roll_matrix(1, 1) + roll_matrix(-1, -1) + roll_matrix(1, -1), roll_matrix(-1, 1)
        grid = np.logical_or(np.logical_and(grid, neighbours == 2), neighbours == 3)
        grid = grid.astype(int)
        yield grid

grid = np.zeros((10, 10))

#R-pentomino
grid[3, 2:4] = 1
grid[4, 1:3] = 1
grid[5, 2] = 1

for x in life(grid, 10):
    print('\n', x)

FFMpegWriter = animation.writers['ffmpeg']
data = dict(title = 'Game of Life')
writer = FFMpegWriter(fps = 10, metadata = data)
fig = plt.figure()
fig.patch.set_facecolor('black')
with writer.saving(fig, 'Game_of_Life.mp4', 200):
    plt.spy(grid)
    plt.axis('off')
    writer.grab_frame()
    plt.clf()
    for x in life(grid, 800):
        plt.spy(x)
        plt.axis('off')
        writer.grab_frame()
        plt.clf()