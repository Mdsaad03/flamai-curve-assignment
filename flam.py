import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
def estimate_parameters(csv_path="xy_data.csv"):
    df = pd.read_csv(csv_path)
    pts_x = df["x"].values
    pts_y = df["y"].values

    def loss(params):
        theta, M, X = params
        u = pts_x - X
        v = pts_y - 42.0
        t = u * np.cos(theta) + v * np.sin(theta)
        perp_actual = -u * np.sin(theta) + v * np.cos(theta)
        perp_pred = np.exp(M * np.abs(t)) * np.sin(0.3 * t)
        return np.mean(np.abs(perp_actual - perp_pred))
    bounds = [
        (0.0, np.radians(50.0)),  
        (-0.05, 0.05),            
        (0.0, 100.0),             
    ]

    res = differential_evolution(loss, bounds, seed=42, popsize=30, maxiter=200)
    
    if res.success:
        theta_opt, M_opt, X_opt = res.x

        print("\nEstimated Parameters::")
        print(
            f"theta : {theta_opt:.6f} rad ({np.degrees(theta_opt):.4f} deg / ~"
            f" {round(np.degrees(theta_opt))} deg)"
        )
        print(f"M     : {M_opt:.6f} (~ {round(M_opt, 2)})")
        print(f"X     : {X_opt:.6f} (~ {round(X_opt, 1)})")
        latex_str = (
            f"\\left(t*\\cos({theta_opt:.4f})-e^{{{M_opt:.4f}\\left|t\\right|}} \\cdot "
            f"\\sin(0.3t)\\sin({theta_opt:.4f})+{X_opt:.4f}, "
            f"42+t*\\sin({theta_opt:.4f})+e^{{{M_opt:.4f}\\left|t\\right|}} \\cdot "
            f"\\sin(0.3t)\\cos({theta_opt:.4f})\\right)"
        )
        print("\nDesmos Link:")
        print(latex_str)

        return theta_opt, M_opt, X_opt
    else:
        print("failed:", res.message)
        return None

if __name__ == "__main__":
    estimate_parameters("xy_data.csv")
