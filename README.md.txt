# Simple Harmonic Motion (SHM) Waveform Visualizer

A Python script that models simple harmonic motion by calculating angular frequency ($\omega$) from physical constants ($k$ = spring constant, $m$ = mass) and plotting position over time using `matplotlib` and `numpy`.

---

## 📐 Math & Physics Fundamentals

The script simulates a classic oscillator executing simple harmonic motion (SHM).

### 1. Angular Frequency ($\omega$)
The rate of oscillation depends entirely on the system's stiffness (spring constant $k$) and mass ($m$):

$$\omega = \sqrt{\frac{k}{m}}$$

### 2. Equation of Motion
Position $y(t)$ as a function of time $t$ with amplitude $a$ is modeled by:

$$y(t) = a \sin(\omega t)$$

---

## 💡 What I Learned & Key Technical Insights

* **Vectorized Math with `numpy`:** Passing the time array `x` directly into `np.sin(w * x)` evaluates position across all time steps instantly without requiring explicit `for` loops.
* **Physics & Code Connection:** Translating the analytical formula $y(t) = a \sin(\omega t)$ directly into Python code requires calculating $\omega = \sqrt{\frac{k}{m}}$ first, connecting mechanical parameters ($k, m$) directly to wave behavior.
* **Handling Frequency Scale:** Large spring constants ($k$) or very small masses ($m$) cause rapid oscillations, requiring high density in `np.linspace` time samples to prevent spatial aliasing on the plot.