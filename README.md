# Parametric Equation Solver & Curve Fitting

A Python script utilizing SciPy's Differential Evolution and L1 loss to estimate unknown parameters ($\theta$, $M$, $X$) of a 2D transformed parametric curve from sampled dataset points.

## Problem Description
This project solves for unknown variables in the following parametric equation of a curve:
$$ x = t * \cos(\theta) - e^{M|t|} * \sin(0.3t)\sin(\theta) + X $$
$$ y = 42 + t * \sin(\theta) + e^{M|t|} * \sin(0.3t)\cos(\theta) $$

Where the constraints are:
* $0^\circ < \theta < 50^\circ$
* $-0.05 < M < 0.05$
* $0 < X < 100$
* $6 < t < 60$

## Methodology
The script recognizes the equations as a rotated and translated version of a base parametric curve. By applying an inverse transformation (rotation and translation) to the provided $(x, y)$ dataset, it isolates the transverse displacement. 

It then uses **Differential Evolution** (a robust global optimizer) to minimize the **L1 distance (Mean Absolute Error)** between the expected and actual transverse displacement, reliably recovering the exact parameters.

## Usage
1. Place your dataset in `xy_data.csv` with columns `x` and `y`.
2. Install dependencies: `pip install numpy pandas scipy`
3. Run the script: `python flam.py`
4. The script will output the optimal parameters and generate a LaTeX string ready to be pasted into [Desmos](https://www.desmos.com/calculator) for plotting.
