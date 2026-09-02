import math
import numpy as np
import pandas as pd
import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #bad5de;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(":blue[Math.sims]", text_alignment="center")

function_type = st.selectbox(
    "Choose a mathematics topic:",
    [
        "Linear Function",
        "Quadratic Function",
        "Reciprocal Function",
        "Exponential Function",
        "Sine Function",
        "Cosine Function",
        "Simple Harmonic Waves",
    ],
)

# Standard math functions requiring x-axis range
if function_type != "Simple Harmonic Waves":
    x_axis = st.number_input("X-axis limit (range from -X to +X):", value=10.0, min_value=0.1)
    num_samples = int(max(100, x_axis * 100))
    x = np.linspace(-x_axis, x_axis, num_samples)

if function_type == "Linear Function":
    m = st.number_input("Slope (m):", value=1.0)
    b = st.number_input("Y-intercept (b):", value=0.0)
    y = m * x + b
    st.line_chart(pd.DataFrame({"y": y}, index=x), color="#AD261C")

elif function_type == "Quadratic Function":
    a = st.number_input("a:", value=1.0)
    b = st.number_input("b:", value=0.0)
    c = st.number_input("c:", value=0.0)
    y = a * x**2 + b * x + c
    st.line_chart(pd.DataFrame({"y": y}, index=x), color="#AD261C")

elif function_type == "Reciprocal Function":
    # Avoid division by zero at x = 0
    x_recip = x[x != 0]
    y = 1 / x_recip
    st.line_chart(pd.DataFrame({"y": y}, index=x_recip), color="#AD261C")

elif function_type == "Exponential Function":
    a = st.number_input("a (Scale factor):", value=1.0)
    b = st.number_input("b (Base):", value=2.0, min_value=0.01)
    x_pos = np.linspace(0, x_axis, num_samples)
    y = a * (b**x_pos)
    st.line_chart(pd.DataFrame({"y": y}, index=x_pos), color="#AD261C")

elif function_type == "Sine Function":
    x_trig = np.linspace(0, x_axis, num_samples)
    y = np.sin(x_trig)
    st.line_chart(pd.DataFrame({"y": y}, index=x_trig), color="#AD261C")

elif function_type == "Cosine Function":
    x_trig = np.linspace(0, x_axis, num_samples)
    y = np.cos(x_trig)
    st.line_chart(pd.DataFrame({"y": y}, index=x_trig), color="#AD261C")

elif function_type == "Simple Harmonic Waves":
    k = st.number_input("Spring constant (k):", value=10.0)
    a = st.number_input("Amplitude (A):", value=1.0)
    t = st.number_input("Time duration (s):", value=10.0)
    m = st.number_input("Mass (kg):", value=1.0)

    if m <= 0:
        st.error("Mass must be greater than 0.")
        st.stop()
    if k <= 0:
        st.error("Spring constant (k) must be greater than 0.")
        st.stop()
    if t <= 0:
        st.error("Time duration must be greater than 0.")
        st.stop()

    num_samples = int(max(100, t * 100))
    time_pts = np.linspace(0, t, num_samples)
    w = math.sqrt(k / m)  # Angular frequency (rad/s)
    f = w / (2 * np.pi)   # Frequency (Hz)

    st.write(f":green[Angular Frequency: {w:.2f} rad/s]")
    st.write(f":green[Frequency: {f:.2f} Hz]")

    y = a * np.sin(w * time_pts)
    st.line_chart(pd.DataFrame({"Displacement x(t)": y}, index=time_pts), color="#AD261C")