import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # thin string
    L_string = 2  # m
    m_string = 0.068 / 1000  # kg
    g = 9.8

    loops = np.array([5, 4, 7, 6])
    loop_length = np.array([0.233, 0.291, 0.178, 0.207])  # m
    hanging_mass = np.array([0.022, 0.036, 0.010, 0.014])  # kg

    mew = m_string / L_string
    wave_length = loop_length * 2
    T = hanging_mass * g
    f = np.sqrt(T / (mew * (wave_length**2)))

    df = pd.DataFrame(
        {
            "Loops": loops,
            "Loop Length (m)": loop_length,
            "Hanging Mass (kg)": hanging_mass,
            "Wave Length (m)": wave_length,
            "T (N)": T,
            "f (hz)": f,
        }
    )
    print(df, end="\n\n")

    plt.figure(figsize=(6, 4))
    x, y = (mew * wave_length**2), T
    plt.scatter(x, y, color="blue", label="data")
    slope, intercept = np.polyfit(x, y, 1)
    plt.plot(
        x,
        slope * x + intercept,
        color="red",
        label=rf"best fit: T=($f^2$ := {slope:.2e})($\mu \lambda^2$)",
    )
    plt.xlabel(r"$\mu \lambda^2$")
    plt.ylabel(r"T (N)")
    plt.legend()
    plt.title("Thin String")
    plt.grid()
    plt.show()

    # yarn
    L_string = 2  # m
    m_string = 1.75 / 1000  # kg
    g = 9.8

    loops = np.array([5, 4, 3, 2])
    loop_length = np.array([0.235, 0.293, 0.382, 0.531])  # m
    hanging_mass = np.array([0.060, 0.095, 0.160, 0.32])  # kg

    mew = L_string / m_string
    wave_length = loop_length * 2
    T = hanging_mass * g
    f = np.sqrt(T / mew * wave_length**2)

    plt.figure(figsize=(6, 4))
    x, y = mew * wave_length**2, T
    plt.scatter(
        x,
        y,
        color="blue",
    )
    slope, intercept = np.polyfit(x, y, 1)
    plt.plot(x, slope * x + intercept, color="red")
    plt.xlabel(r"$\mu \lambda^2$")
    plt.ylabel(r"T (N)")
    plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
