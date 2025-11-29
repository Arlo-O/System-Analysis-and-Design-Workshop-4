"""
simulation_ca.py

Simple 2D Cellular Automata for Workshop 4.
Rules:
- cell = 1 if sum(neighbors) >= threshold
- optional noise flips states randomly
"""

import numpy as np
from scipy.signal import convolve2d

# -----------------------------
# One step of CA evolution
# -----------------------------
def step(grid, thresh=3, p_noise=0.02):
    kernel = np.ones((3, 3))
    neigh = convolve2d(grid, kernel, mode="same", boundary="wrap") - grid
    new = (neigh >= thresh).astype(int)

    # random noise flip
    if p_noise > 0:
        noise = (np.random.rand(*grid.shape) < p_noise).astype(int)
        new = np.logical_xor(new, noise).astype(int)

    return new

# -----------------------------
# Run CA for N steps
# -----------------------------
def run_ca(initial_grid, steps=40, thresh=3, p_noise=0.02):
    grids = [initial_grid.copy()]
    g = initial_grid.copy()

    for _ in range(steps):
        g = step(g, thresh, p_noise)
        grids.append(g.copy())

    return grids

# -----------------------------
# Demo
# -----------------------------
if __name__ == "__main__":
    np.random.seed(1)
    grid = (np.random.rand(60, 60) < 0.2).astype(int)
    result = run_ca(grid, steps=30)
    print("Generated", len(result), "CA steps")
