"""
simulation_ml.py

Data-driven simulation for Workshop 4.
Uses scikit-learn RandomForest if available.
Replace load_data() path with your real GEFCom2012 dataset location.
"""

import numpy as np
import pandas as pd

# -----------------------------
# Utility: RMSE
# -----------------------------
def rmse(y_true, y_pred):
    return np.sqrt(((y_true - y_pred) ** 2).mean())

# -----------------------------
# Load dataset
# -----------------------------
def load_data(farm=1):
    """
    Loads real GEFCom2012 data for a given wind farm (1–7).

    farm=1 → uses wp1 and windforecast_wf1.csv
    farm=2 → uses wp2 and windforecast_wf2.csv
    ...
    """

    # 1. Load targets (train.csv)
    df_train = pd.read_csv("data/train.csv")

    # target column (wp1, wp2, ..., wp7)
    target_col = f"wp{farm}"
    y = df_train[target_col].values

    # 2. Load weather forecasts for same farm
    df_wf = pd.read_csv(f"data/windforecasts_wf{farm}.csv")

    # Features used: u, v, ws, wd (you can add more later)
    X = df_wf[["u", "v", "ws", "wd"]].values

    # Ensure shapes match
    n = min(len(X), len(y))
    X = X[:n]
    y = y[:n]

    return X, y


# -----------------------------
# Train + Evaluate model
# -----------------------------
def train_and_evaluate(X_train, y_train, X_val, y_val, use_rf=True, random_state=42):
    try:
        if use_rf:
            from sklearn.ensemble import RandomForestRegressor
            model = RandomForestRegressor(n_estimators=70, random_state=random_state)
        else:
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()

        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        return rmse(y_val, preds), model

    except Exception:
        # Fallback linear regression (numpy lstsq)
        X_design = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        coef, *_ = np.linalg.lstsq(X_design, y_train, rcond=None)

        def predict(X):
            Xd = np.hstack([np.ones((X.shape[0], 1)), X])
            return Xd.dot(coef)

        preds = predict(X_val)
        return rmse(y_val, preds), ("linear_coef", coef)

# -----------------------------
# Demo
# -----------------------------
if __name__ == "__main__":
    # Load real data for wind farm 1
    X, y = load_data(farm=1)

    # Train/test split
    split = int(len(X) * 0.7)
    X_train, X_val = X[:split], X[split:]
    y_train, y_val = y[:split], y[split:]

    rmse_value, model = train_and_evaluate(X_train, y_train, X_val, y_val)

    print(f"Real dataset RMSE (farm 1): {rmse_value}")
