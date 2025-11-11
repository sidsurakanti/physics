import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    m = np.array([0.05, 0.10, 0.15, 0.20, 0.25])  # kg
    g = 9.8
    F = m * g  # N

    x0 = 47 / 100  # initial x in m
    x1 = np.array([53.5, 59.1, 65.3, 70.2, 76.3]) / 100
    x2 = np.array([53.1, 59.4, 64.9, 70.3, 76.2]) / 100
    x_avg = (x1 + x2) / 2
    dx = x_avg - x0  # displacement

    print("Initial position (m): ", x0)

    static_df = pd.DataFrame(
        {
            "m (kg)": m,
            "x1 (cm)": x1,
            "x2 (cm)": x2,
            "Δx (m)": dx,
            "F (N)": F,
        }
    )

    print(static_df, end="\n\n")

    plt.figure(figsize=(6, 4))
    plt.scatter(dx, F, color="blue", label="Data")
    slope, intercept = np.polyfit(dx, F, 1)
    plt.plot(dx, slope * dx + intercept, "r--", label=f"Best fit: k={slope:.2f} N/m")
    plt.xlabel("Δx (m)")
    plt.ylabel("F (N)")
    plt.title("Hooke’s Law: Force vs. Displacement")
    plt.legend()
    plt.grid(True)
    plt.show()

    m_dyn = np.array([0.05, 0.07, 0.10, 0.12, 0.14, 0.15, 0.17, 0.19, 0.21, 0.23])
    T = np.array(
        [0.8480, 0.8891, 0.963, 1.0118, 1.056, 1.0753, 1.119, 1.1572, 1.2024, 1.2367]
    )

    k_dynamic = 4 * (np.pi**2) * m_dyn / (T**2)
    k2 = k_dynamic**2
    avg_k = np.mean(k_dynamic)
    std_k = np.std(k_dynamic, ddof=1)

    dynamic_df = pd.DataFrame(
        {"m (kg)": m_dyn, "T (s)": T, "k (N/m)": k_dynamic, "k² (N²/m²)": k2}
    )

    print(dynamic_df, end="\n\n")
    print("Average K: ", round(avg_k, 3))
    print("Stdev K: ", round(std_k, 3))


if __name__ == "__main__":
    main()
