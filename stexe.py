import math
import numpy as np
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Set up CustomTkinter appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class MathSimsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Math.sims")
        self.geometry("1100x700")
        self.configure(fg_color="#bad5de")

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar / Controls Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=320, corner_radius=0, fg_color="#a2c4ce")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Math.sims", 
            font=ctk.CTkFont(size=22, weight="bold"), 
            text_color="#1f4e5b"
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.topic_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Choose a mathematics topic:", 
            font=ctk.CTkFont(size=14, weight="bold"), 
            text_color="#2b2b2b"
        )
        self.topic_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

        self.function_types = [
            "Linear Function",
            "Quadratic Function",
            "Reciprocal Function",
            "Exponential Function",
            "Sine Function",
            "Cosine Function",
            "Simple Harmonic Waves",
        ]
        
        self.function_var = ctk.StringVar(value=self.function_types[0])
        self.topic_menu = ctk.CTkOptionMenu(
            self.sidebar_frame, 
            values=self.function_types, 
            variable=self.function_var,
            command=self.on_function_change,
            fg_color="#3b7a8c",
            button_color="#2f6371",
            button_hover_color="#234c56"
        )
        self.topic_menu.grid(row=2, column=0, padx=20, pady=(5, 15), sticky="ew")

        # Container for dynamic parameter inputs
        self.inputs_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.inputs_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        self.inputs_frame.grid_columnconfigure(0, weight=1)

        # Info / Output text label
        self.info_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="", 
            font=ctk.CTkFont(size=13, weight="bold"), 
            text_color="#1f4e5b", 
            justify="left"
        )
        self.info_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        # --- Main Plot Area ---
        self.plot_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=10)
        self.plot_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.plot_frame.grid_columnconfigure(0, weight=1)
        self.plot_frame.grid_rowconfigure(0, weight=1)

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        self.fig.patch.set_facecolor('white')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Initialize inputs and plot
        self.build_inputs()
        self.update_plot()

    def clear_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()
        self.info_label.configure(text="")

    def on_function_change(self, choice):
        self.build_inputs()
        self.update_plot()

    def add_number_input(self, parent, label_text, default_val):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=5)
        
        lbl = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=12), text_color="#2b2b2b")
        lbl.pack(side="left", padx=(0, 10))
        
        entry = ctk.CTkEntry(frame, width=100, fg_color="white", text_color="black")
        entry.insert(0, str(default_val))
        entry.pack(side="right")
        entry.bind("<KeyRelease>", lambda e: self.update_plot())
        return entry

    def build_inputs(self):
        self.clear_inputs()
        ft = self.function_var.get()

        if ft != "Simple Harmonic Waves":
            self.entry_xaxis = self.add_number_input(self.inputs_frame, "X-axis limit (-X to +X):", 10.0)

        if ft == "Linear Function":
            self.entry_m = self.add_number_input(self.inputs_frame, "Slope (m):", 1.0)
            self.entry_b = self.add_number_input(self.inputs_frame, "Y-intercept (b):", 0.0)

        elif ft == "Quadratic Function":
            self.entry_a = self.add_number_input(self.inputs_frame, "a:", 1.0)
            self.entry_b = self.add_number_input(self.inputs_frame, "b:", 0.0)
            self.entry_c = self.add_number_input(self.inputs_frame, "c:", 0.0)

        elif ft == "Reciprocal Function":
            pass  # Uses only x_axis

        elif ft == "Exponential Function":
            self.entry_a = self.add_number_input(self.inputs_frame, "a (Scale):", 1.0)
            self.entry_b = self.add_number_input(self.inputs_frame, "b (Base):", 2.0)

        elif ft in ["Sine Function", "Cosine Function"]:
            pass  # Uses only x_axis

        elif ft == "Simple Harmonic Waves":
            self.entry_k = self.add_number_input(self.inputs_frame, "Spring constant (k):", 10.0)
            self.entry_a = self.add_number_input(self.inputs_frame, "Amplitude (A):", 1.0)
            self.entry_t = self.add_number_input(self.inputs_frame, "Time duration (s):", 10.0)
            self.entry_m = self.add_number_input(self.inputs_frame, "Mass (kg):", 1.0)

    def get_float(self, entry, default=1.0):
        try:
            return float(entry.get())
        except ValueError:
            return default

    def update_plot(self):
        ft = self.function_var.get()
        self.ax.clear()
        self.ax.set_facecolor('#f8f9fa')
        self.ax.grid(True, linestyle='--', alpha=0.6)

        try:
            if ft != "Simple Harmonic Waves":
                x_axis = max(0.1, self.get_float(self.entry_xaxis, 10.0))
                num_samples = int(max(100, x_axis * 100))
                x = np.linspace(-x_axis, x_axis, num_samples)

            if ft == "Linear Function":
                m = self.get_float(self.entry_m, 1.0)
                b = self.get_float(self.entry_b, 0.0)
                y = m * x + b
                self.ax.plot(x, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Linear Function: y = mx + b", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")

            elif ft == "Quadratic Function":
                a = self.get_float(self.entry_a, 1.0)
                b = self.get_float(self.entry_b, 0.0)
                c = self.get_float(self.entry_c, 0.0)
                y = a * x**2 + b * x + c
                self.ax.plot(x, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Quadratic Function: y = ax² + bx + c", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")

            elif ft == "Reciprocal Function":
                x_recip = x[x != 0]
                y = 1 / x_recip
                self.ax.plot(x_recip, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Reciprocal Function: y = 1/x", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")
                self.ax.set_ylim(-10, 10)

            elif ft == "Exponential Function":
                a = self.get_float(self.entry_a, 1.0)
                b = self.get_float(self.entry_b, 2.0)
                x_pos = np.linspace(0, x_axis, num_samples)
                y = a * (b**x_pos)
                self.ax.plot(x_pos, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Exponential Function: y = a·bˣ", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")

            elif ft == "Sine Function":
                x_trig = np.linspace(0, x_axis, num_samples)
                y = np.sin(x_trig)
                self.ax.plot(x_trig, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Sine Function: y = sin(x)", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")

            elif ft == "Cosine Function":
                x_trig = np.linspace(0, x_axis, num_samples)
                y = np.cos(x_trig)
                self.ax.plot(x_trig, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Cosine Function: y = cos(x)", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")

            elif ft == "Simple Harmonic Waves":
                k = self.get_float(self.entry_k, 10.0)
                a_amp = self.get_float(self.entry_a, 1.0)
                t_dur = self.get_float(self.entry_t, 10.0)
                m_mass = self.get_float(self.entry_m, 1.0)

                if m_mass <= 0 or k <= 0 or t_dur <= 0:
                    self.info_label.configure(text="Error: Mass, k, and Time must be > 0", text_color="red")
                    self.canvas.draw()
                    return

                num_samples = int(max(100, t_dur * 100))
                time_pts = np.linspace(0, t_dur, num_samples)
                w = math.sqrt(k / m_mass)
                f_freq = w / (2 * np.pi)

                self.info_label.configure(
                    text=f"Angular Frequency: {w:.2f} rad/s\nFrequency: {f_freq:.2f} Hz",
                    text_color="#1f4e5b"
                )

                y = a_amp * np.sin(w * time_pts)
                self.ax.plot(time_pts, y, color="#AD261C", linewidth=2.5)
                self.ax.set_title("Simple Harmonic Wave: x(t) = A·sin(ωt)", color="#1f4e5b", fontsize=14, fontweight="bold")
                self.ax.set_xlabel("Time (s)")
                self.ax.set_ylabel("Displacement x(t)")

        except Exception:
            pass

        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    app = MathSimsApp()
    app.mainloop()