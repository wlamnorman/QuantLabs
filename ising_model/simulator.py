import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


GRID_SIZE = 50
beta = 0.4  # inverse temperature (beta = 1/kT, where k is Boltzmann's constant and T is temperature)
grid = np.random.choice([-1, 1], (GRID_SIZE, GRID_SIZE))  # random initial grid


def main():
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation="nearest", cmap="coolwarm")
    ani = animation.FuncAnimation(
        fig, animate, fargs=(img,), frames=None, interval=200, blit=True
    )
    plt.show()


def ising_step(grid, beta):
    "Perform one Monte Carlo step using the Metropolis-Hastings algorithm"
    for _ in range(GRID_SIZE * GRID_SIZE):
        i, j = np.random.randint(0, GRID_SIZE, 2)
        dE = (
            2
            * grid[i, j]
            * (
                grid[(i + 1) % GRID_SIZE, j]
                + grid[(i - 1) % GRID_SIZE, j]
                + grid[i, (j + 1) % GRID_SIZE]
                + grid[i, (j - 1) % GRID_SIZE]
            )
        )
        if dE < 0 or np.random.rand() < np.exp(-dE * beta):
            grid[i, j] *= -1


def animate(frame, img):
    ising_step(grid, beta)
    img.set_array(grid)
    return (img,)


if __name__ == "__main__":
    main()
