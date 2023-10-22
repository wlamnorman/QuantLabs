# Conway's game of life
Game of life is a cellular automaton (CA), meaning a grid of cells that can be in a finite number of states that is updated by application of some function iteratively.

What makes game of life interesting I think are the fact that the CA is
* `Turing complete`: it is capable of implementing any algorithm.
* a `self-replicating machine / universal constructor`: clusters of cells in the grid may reproduce autonomously based on their environment.

## Implementation
`simulator.py` contains an implementation of the following replication rules of game of life on a toroidal grid:

1. Any live cell with two or three live neighbours
survives.
2. Any dead cell with three live neighbours becomes
 a live cell.
3. All other live cells die in the next generation.
Similarly, all other dead cells stay dead.

Running the script starts a simulation that will go on until the window is closed by the user.