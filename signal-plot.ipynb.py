import numpy as np
import matplotlib.pyplot as plt

N_SAMPLES = 500
input_range = np.linspace(0, 2 * np.pi, N_SAMPLES, dtype=float)
signal = np.sin(input_range)

noise = np.random.normal(0.5, 1, N_SAMPLES)
assert noise.shape == input_range.shape

noisy_signal = signal + noise / 5

plt.plot(input_range, noisy_signal, 'b.', alpha=0.5)
plt.plot(input_range, signal, 'r-', linewidth=4)
plt.legend(['Sensor readings', 'Truth'])
plt.xlabel('Time')
plt.ylabel('Value of thing we care about')

plt.show()
# %%
