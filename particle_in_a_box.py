import matplotlib.pyplot as plt
import numpy as np

# System parameters
L = 1.0
x = np.linspace(0, L, 1000)

plt.figure(figsize=(9, 6))

# Plot wave functions psi_n(x)
plt.subplot(2, 1, 1)
for n in range(1, 5):
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    plt.plot(x, psi_n, label=f"n = {n}")

plt.title(r"Wave function $\psi(x)$")
plt.ylabel(r"$\psi_n(x)$")
plt.xlim(0, L)
plt.grid(True)
plt.legend(loc="upper right")

# Plot probability densities |psi_n(x)|^2
plt.subplot(2, 1, 2)
for n in range(1, 5):
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    prob_density = psi_n**2
    plt.plot(x, prob_density, label=f"n = {n}")

plt.title(r"Probability density $|\psi(x)|^2$")
plt.xlabel(f"Position x (box width L = {L})")
plt.ylabel(r"$|\psi_n(x)|^2$")
plt.xlim(0, L)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()