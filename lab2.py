import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def main():
    g_standard = 9.81
    delta_x = 48.70 / 100  # meters

    m_hang = [0.02, 0.03, 0.04, 0.05, 0.06]  # kg
    m_cart = 0.5343  # kg

    times_df = np.array(
        [
            [1.6347, 1.5651, 1.5787, 1.5292, 1.5581],
            [1.2590, 1.2396, 1.2452, 1.2366, 1.2586],
            [1.0690, 1.0747, 1.0711, 1.1014, 1.0801],
            [0.9374, 0.9318, 0.9388, 0.9619, 0.9455],
            [0.8687, 0.8669, 0.8760, 0.8790, 0.8601],
        ]
    )

    rows = []
    for i, m_hi in enumerate(m_hang):
        times = times_df[i]
        t_avg = np.mean(times)

        a_exp = 2 * delta_x / t_avg**2
        a_theo = (m_hi * g_standard) / (m_cart + m_hi)
        percent_diff = abs(a_exp - a_theo) / a_theo * 100

        rows.append((m_hi, t_avg, a_exp, a_theo, percent_diff))

    data_df = pd.DataFrame(times_df, index=m_hang)  # type: ignore
    print("%%%%%%% RAW DATA %%%%%%%%%\n", data_df)

    results_df = pd.DataFrame(
        rows,
        columns=[
            "m_hang (kg)",
            "Avg Time (s)",
            "a_exp (m/s^2)",
            "a_theo (m/s^2)",
            "% Diff",
        ],  # type: ignore
    )

    print("\n%%%%% RESULTS %%%%%")
    print(results_df.to_string(index=False))

    # forces = m_hang * g
    forces = results_df["m_hang (kg)"] * g_standard

    plt.plot(results_df["a_exp (m/s^2)"], forces, "o-", label="Experimental")
    plt.plot(results_df["a_theo (m/s^2)"], forces, "s-", label="Theoretical")

    coeffs_exp = np.polyfit(results_df["a_exp (m/s^2)"], forces, 1)
    slope_exp, intercept_exp = coeffs_exp
    fit_exp = np.poly1d(coeffs_exp)

    coeffs_theo = np.polyfit(results_df["a_theo (m/s^2)"], forces, 1)
    slope_theo, intercept_theo = coeffs_theo
    fit_theo = np.poly1d(coeffs_theo)

    print(
        f"\nLinear regression (Experimental): F = {slope_exp:.4f} * a + {intercept_exp:.4f}"
    )
    print(
        f"Linear regression (Theoretical):  F = {slope_theo:.4f} * a + {intercept_theo:.4f}"
    )

    x_vals = np.linspace(
        min(results_df["a_exp (m/s^2)"].min(), results_df["a_theo (m/s^2)"].min()),
        max(results_df["a_exp (m/s^2)"].max(), results_df["a_theo (m/s^2)"].max()),
        100,
    )

    plt.plot(
        x_vals,
        fit_exp(x_vals),
        "--",
        label=f"Exp Fit: F = {slope_exp:.3f}a + {intercept_exp:.3f}",
    )
    plt.plot(
        x_vals,
        fit_theo(x_vals),
        "--",
        label=f"Theo Fit: F = {slope_theo:.3f}a + {intercept_theo:.3f}",
    )

    plt.xlabel("Acceleration (m/s^2)")
    plt.ylabel("Force (N)")
    plt.title("Force vs Acceleration with Fits")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
