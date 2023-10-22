import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GRID_SIZE: int = 100
ALIVE: int = 1
DEAD: int = 0
P_START_ALIVE: float = 0.25


def forever_update(frame, img, grid, N):
    """Indefinite update of Conway's Game of Life grid"""
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # adjacent cells
            total = int(
                (  # toroidal grid
                    grid[i, (j - 1) % GRID_SIZE]
                    + grid[i, (j + 1) % GRID_SIZE]
                    + grid[(i - 1) % GRID_SIZE, j]
                    + grid[(i + 1) % GRID_SIZE, j]
                    + grid[(i - 1) % GRID_SIZE, (j - 1) % GRID_SIZE]
                    + grid[(i - 1) % GRID_SIZE, (j + 1) % GRID_SIZE]
                    + grid[(i + 1) % GRID_SIZE, (j - 1) % GRID_SIZE]
                    + grid[(i + 1) % GRID_SIZE, (j + 1) % GRID_SIZE]
                )
            )

            if grid[i, j] == ALIVE:
                if total < 2 or total > 3:
                    new_grid[i, j] = DEAD
            else:
                if total == 3:
                    new_grid[i, j] = ALIVE

    img.set_data(new_grid)
    grid[:] = new_grid[:]  # transfer elements
    return (img,)


grid = np.random.choice(
    [ALIVE, DEAD], GRID_SIZE * GRID_SIZE, p=[P_START_ALIVE, (1 - P_START_ALIVE)]
).reshape(GRID_SIZE, GRID_SIZE)


fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation="nearest", cmap="gray")
ani = animation.FuncAnimation(
    fig,
    forever_update,
    fargs=(img, grid, GRID_SIZE),
    frames=None,
    interval=200,
    blit=True,
    cache_frame_data=False,
)

plt.show()
