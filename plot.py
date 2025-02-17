import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("txt/brownian_motion_path.txt")
time = data[:, 0]
prices = data[:, 1]

plt.style.use("dark_background")
plt.figure(figsize=(10, 5))
plt.plot(time, prices, label="GBM Stock Path", color="white", linewidth=2)

plt.xlabel("Time (Days)")
plt.ylabel("Stock Price")
plt.title("Simulated Geometric Brownian Motion (Stock Price Path)")
plt.legend()

plt.show()
