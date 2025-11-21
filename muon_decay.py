import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Define the Monte Carlo simulation function
def muon_monte_carlo_rest_frame(n0, lmbda, steps):
    decay_mc = np.zeros(steps)  # to store N at each step
    n = n0                      # current number of particles
    t_half_mc = None            # simulated half-life (step count)

    for t in range(steps):
        decay_mc[t] = n
        decayd = np.sum(np.random.rand(n) < lmbda)  # count decayed particles
        n = n - decayd

        if t_half_mc is None and n < n0 / 2:
            t_half_mc = t

    return decay_mc, t_half_mc

# Parameters
n0 = 1000
t_half = 2.2  # half-life in seconds
lmbda = np.log(2) / t_half          # decay constant
steps = 200            # number of simulation steps

# Run the Monte Carlo simulation
decay_mc, t_half_mc = muon_monte_carlo_rest_frame(n0, lmbda, steps)
time_array = np.arange(steps)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_array, decay_mc, label='$\mu$ Decay in rest frame', color='blue', marker='o', markersize=3)
plt.xlabel('Time ($\mu s$)')
plt.ylabel('Number of Particles')
plt.title('Monte Carlo Simulation of $\mu$ Decay')
plt.grid(True)
plt.legend()
plt.show()

print("Simulated Half-life: ", t_half_mc)
print("Theoretical Half-life :", t_half)