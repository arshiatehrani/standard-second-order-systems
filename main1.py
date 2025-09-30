import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step

# Define parameters (omega_n is fixed)
omega_n = 5.0 
t = np.linspace(0, 5, 500)

# Define damping ratios for each case
zetas = {
    'Undamped (ζ=0)': 0.0,
    'Underdamped (ζ=0.2)': 0.2,
    'Critically Damped (ζ=1)': 1.0,
    'Overdamped (ζ=2)': 2.0
}

plt.figure(figsize=(10, 6))
plt.title('Unit Step Response Comparison (ωn = 5 rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('Output c(t)')
plt.axhline(1.0, color='black', linestyle='--', label='Final Value')

# Simulate and plot responses
for label, zeta in zetas.items():
    # Transfer function: wn^2 / (s^2 + 2*zeta*wn*s + wn^2)
    numerator = [omega_n**2]
    denominator = [1, 2*zeta*omega_n, omega_n**2]
    
    # Get the step response
    # The actual Python function call would be like: T, Y = control.step_response(control.TransferFunction(numerator, denominator), T=t)
    # We use a conceptual plot for the output here:
    
    # Placeholder for actual response calculation (Conceptual Plot)
    if zeta == 0:
        c_t = 1 - np.cos(omega_n * t)
    elif 0 < zeta < 1:
        wd = omega_n * np.sqrt(1 - zeta**2)
        phi = np.arctan(np.sqrt(1 - zeta**2) / zeta)
        c_t = 1 - (np.exp(-zeta * omega_n * t) / np.sqrt(1 - zeta**2)) * np.sin(wd * t + phi)
    elif zeta == 1:
        c_t = 1 - (1 + omega_n * t) * np.exp(-omega_n * t)
    else: # zeta > 1
        s1 = -zeta * omega_n + omega_n * np.sqrt(zeta**2 - 1)
        s2 = -zeta * omega_n - omega_n * np.sqrt(zeta**2 - 1)
        c_t = 1 - (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t)) / (s2 - s1)

    plt.plot(t, c_t, label=label)

plt.legend()
plt.grid(True)
plt.show()