# GEFCom2012 Wind Forecasting System - Workshop 4 Simulations

[![Workshop 4](https://img.shields.io/badge/Workshop-4-blue)]()
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

## Overview

This repository contains the implementation and results of computational simulations for the GEFCom2012 wind forecasting system, developed as part of **Workshop 4** in the Systems Analysis & Design course. The simulations validate the MLOps architecture designed in previous workshops by demonstrating both data-driven and event-based approaches to modeling the system's behavior.

## Repository Structure

```
Workshop_4_Simulation/
├── plots/
│   ├── rmse_plot.png        # ML simulation RMSE visualization
│   └── ca_evolution.png     # Cellular Automata evolution heatmap
├── demo_run.py              # Main script to execute both simulations
├── simulation_ml.py         # ML-based simulation implementation
├── simulation_ca.py         # Cellular Automata simulation implementation
├── Workshop_4_Report.pdf    # Final simulation report
└── requirements.txt         # Python dependencies
```

## Dependencies

```bash
numpy>=1.21.0
matplotlib>=3.4.0
pandas>=1.3.0
scikit-learn>=1.0.0
scipy>=1.7.0
```

## How to Run Simulations

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Execute the simulations:
```bash
python demo_run.py
```

3. View the generated plots in the `plots/` directory and the final report.

## Key Results

### ML Simulation Results
- **Baseline RMSE (70 trees)**: 0.172279
- **With 100 trees**: 0.1709 (improved stability)
- **With 30 trees**: 0.1789 (reduced stability)

The ML model demonstrated significant sensitivity to hyperparameter changes, confirming the chaotic nature of wind forecasting systems.

### CA Simulation Results
The cellular automaton simulation demonstrated three distinct behaviors based on noise levels:
- **Low noise (0.0)**: Stable structures with minimal evolution
- **Moderate noise (0.02)**: Irregular transitions and oscillations
- **High noise (0.05)**: Fully chaotic propagation across the grid

## Design Validation

Both simulations validated key components of our MLOps architecture:

| Characteristic | ML Simulation | CA Simulation |
|---------------|---------------|---------------|
| Nature of Chaos | Deterministic Chaos (Input Sensitivity) | Systemic Chaos (Emergent Propagation) |
| Key Finding | Sensitivity and Error Instability | Chaotic Propagation of Failures |
| Validated Component | Monitoring Layer and Retraining Control | Data Ingestion/Validation and Fault Isolation |

## Design Improvements

Based on simulation results, the following improvements are recommended:

1. **Strengthen Data Validation**: Implement spatial cross-validation to detect and isolate inconsistencies between correlated wind farms.

2. **Probabilistic Forecasting**: Migrate to Quantile Regression or Bayesian Neural Networks to transform uncertainty into prediction intervals.

## Autors 
Tomás Cárdenas Benítez – 20221020021
Diego Angelo Ruano Vergara – 20242020278
Sebastian David Trujillo Vargas – 20242020217
Arlo Nicolas Ocampo Gallego – 20221020104

---
*Developed as part of the Systems Analysis & Design course at Universidad Distrital Francisco José de Caldas*  
*Instructor: Eng. Carlos Andrés Sierra, M.Sc.*  
*November 2025*
