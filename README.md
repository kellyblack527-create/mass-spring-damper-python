# Mass-Spring-Damper Simulation (Python)

A second-order dynamic system simulated in Python using NumPy and Matplotlib.
Euler's method is implemented manually to solve the ODE — no solvers, no Simulink.

## System Parameters
- Mass: m = 1.0 kg
- Damping coefficient: c = 0.5 Ns/m
- Spring stiffness: k = 4.0 N/m
- Initial displacement: x₀ = 1.0 m
- Initial velocity: v₀ = 0.0 m/s

## Governing Equation
a = (F - c·v - k·x) / m 
## What the Plot Shows
An underdamped response — the system oscillates and gradually settles to zero.
The damping ratio is low enough to allow oscillation but high enough to kill it over time.

## Tools Used
- Python 3.14
- NumPy
- Matplotlib

## Context
This is Step 1 of a larger **Vehicle Data Analysis** project being built in Python.
The goal is to apply engineering simulation and data analysis skills to real vehicle dynamics problems.
