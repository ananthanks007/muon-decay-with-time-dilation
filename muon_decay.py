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
n0 = 1000000
t_half = 2.2*10**-6  # half-life in seconds
lmbda = np.log(2) / t_half          # decay constant
steps = 20              # number of simulation steps

# Run the Monte Carlo simulation
decay_mc, t_half_mc = muon_monte_carlo_rest_frame(n0, lmbda, steps)
time_array = np.arange(steps)
time_array = time_array * (t_half / (steps / 10))  # scale time array for better visualization

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_array, decay_mc, label='Monte Carlo Simulation of $\mu$ Decay', color='blue', marker='o', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('Number of Particles')
plt.title('Monte Carlo Simulation of Radioactive Decay')
# plt.xlim(0,300) # To make the graph neater in case if the t-half is small
plt.grid(True)
plt.legend()
plt.show()

print("Simulated Half-life: ", t_half_mc)
print("Theoretical Half-life :", t_half)