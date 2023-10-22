import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def ising_step(grid, beta):
    "Perform one Monte Carlo step using the Metropolis-Hastings algorithm"
    N = len(grid)
    for _ in range(N * N):
        i, j = np.random.randint(0, N, 2)
        dE = (
            2
            * grid[i, j]
            * (
                grid[(i + 1) % N, j]
                + grid[(i - 1) % N, j]
                + grid[i, (j + 1) % N]
                + grid[i, (j - 1) % N]
            )
        )
        if dE < 0 or np.random.rand() < np.exp(-dE * beta):
            grid[i, j] *= -1


# Initialize parameters and grid
N = 50  # Grid size
beta = 0.4  # Inverse temperature (beta = 1/kT, where k is Boltzmann's constant and T is temperature)
grid = np.random.choice([-1, 1], (N, N))  # Random initial configuration

# Create figure and axis
fig, ax = plt.subplots()

# Set up the initial plot
img = ax.imshow(grid, interpolation="nearest", cmap="coolwarm")


def animate(frame):
    ising_step(grid, beta)
    img.set_array(grid)
    return (img,)


# Animate indefinitely
ani = animation.FuncAnimation(fig, animate, frames=None, interval=200, blit=True)

plt.show()
