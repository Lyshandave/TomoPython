# ============================================================
# Heat Diffusion Simulation
# Computational Science Laboratory
# One-Dimensional Heat Equation
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# PARAMETERS
# ------------------------------------------------------------
rod_length = 100      # Number of spatial points
time_steps = 200      # Number of simulation steps
alpha = 0.25          # Thermal diffusivity
dx = 1                # Distance between points
dt = 0.4              # Time interval

# ------------------------------------------------------------
# STABILITY CONDITION
# ------------------------------------------------------------
r = alpha * dt / (dx ** 2)

if r > 0.5:
    print("Warning: Simulation may become unstable.")

# ------------------------------------------------------------
# INITIAL TEMPERATURE DISTRIBUTION
# ------------------------------------------------------------
temperature = np.zeros(rod_length)

# Heat the center of the rod
temperature[45:55] = 100

# Save initial state
history = [temperature.copy()]

# ------------------------------------------------------------
# SIMULATION
# ------------------------------------------------------------
for step in range(time_steps):

    new_temperature = temperature.copy()

    for i in range(1, rod_length - 1):

        new_temperature[i] = (
            temperature[i]
            + r * (
                temperature[i + 1]
                - 2 * temperature[i]
                + temperature[i - 1]
            )
        )

    temperature = new_temperature

    # Save temperature distribution
    history.append(temperature.copy())

# ------------------------------------------------------------
# DISPLAY FINAL TEMPERATURES
# ------------------------------------------------------------
print("\nFinal Temperature Distribution\n")

for i in range(0, rod_length, 5):
    print(f"Position {i:3d}: {temperature[i]:6.2f} °C")

# ------------------------------------------------------------
# PLOT INITIAL AND FINAL TEMPERATURES
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))

plt.plot(history[0], label="Initial Temperature")
plt.plot(history[-1], label="Final Temperature")

plt.title("Heat Diffusion Along a Metal Rod")
plt.xlabel("Position Along Rod")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# ANIMATION-LIKE SNAPSHOTS
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))

snapshots = [0, 20, 50, 100, 150, 200]

for s in snapshots:
    plt.plot(history[s], label=f"Step {s}")

plt.title("Heat Diffusion Over Time")
plt.xlabel("Position Along Rod")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()