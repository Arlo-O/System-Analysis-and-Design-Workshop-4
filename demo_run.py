"""
demo_run.py
Runs a synthetic demo for ML + CA simulations.
Generates:
- plots/rmse_plot.png
- plots/ca_evolution.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from simulation_ml import train_and_evaluate
from simulation_ca import run_ca

# -----------------------------
# Output folders
# -----------------------------
BASE = Path(__file__).parent
PLOTS = BASE / "plots"
PLOTS.mkdir(exist_ok=True)

# -----------------------------
# ML Demo
# -----------------------------
def run_ml_demo():
    n = 1000
    np.random.seed(0)
    X = np.random.randn(n, 5)
    y = np.sin(X[:, 0]) + 0.3*X[:, 1]**2 - 0.15*X[:, 2] + 0.1*np.random.randn(n)

    split = int(n * 0.75)
    X_train, X_val = X[:split], X[split:]
    y_train, y_val = y[:split], y[split:]

    score, model = train_and_evaluate(X_train, y_train, X_val, y_val)

    # RMSE plot
    plt.figure()
    plt.plot([0, 1], [score, score], label=f"RMSE={score:.4f}")
    plt.title("Synthetic ML RMSE")
    plt.legend()
    plt.savefig(PLOTS / "rmse_plot.png")
    plt.close()

    return score

# -----------------------------
# CA Demo
# -----------------------------
def run_ca_demo():
    np.random.seed(2)
    init = (np.random.rand(60, 60) < 0.18).astype(int)
    grids = run_ca(init, steps=40, thresh=3, p_noise=0.02)

    # evolution heatmap
    evolution = sum(grids)

    plt.figure(figsize=(6, 5))
    plt.imshow(evolution, origin="lower")
    plt.title("CA Visit Count Heatmap")
    plt.colorbar()
    plt.savefig(PLOTS / "ca_evolution.png")
    plt.close()

    return evolution

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("Running ML demo...")
    rmse = run_ml_demo()
    print("ML RMSE:", rmse)

    print("Running CA demo...")
    evo = run_ca_demo()
    print("CA evolution shape:", evo.shape)
