import matplotlib.pyplot as plt
import numpy as np
import math

k = float(input("Enter the value of k: "))#constant
a = float(input("Enter the value of a: "))#amplitude
t = float(input("Enter the value of t: "))#time
m = float(input("Enter the value of m: "))#mass
if m <= 0:
    raise ValueError("Mass must be greater than 0.")
if k <= 0:
    raise ValueError("Spring constant (k) must be greater than 0.")
num_samples = int(max(100, t * 100)) # Ensures smooth line regardless of t
x = np.linspace(0, t, num_samples)
w = math.sqrt(k / m)
y = a * np.sin(w * x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, "r-", label=f"w = {w:.2f} rad/s")
plt.title("Simple Harmonic Motion")
plt.xlabel("Time (s)")
plt.ylabel("Displacement")
plt.grid(True)
plt.legend()
plt.show()
