import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    r = np.array([0.14, 0.16, 0.18, 0.2]).reshape(-1, 1)
    # T_all = np.ones((4, 3))
    T_all = np.array(
        [
            [19.31, 20.78, 22.03],
            [13.81, 15.69, 14.53],
            [8.28, 7.31, 7.50],
            [6.68, 6.41, 6.32],
        ]
    )
    T_avg = np.mean(T_all, axis=1, keepdims=True)
    T = T_avg / 15
    a = (4 * (3.14**2) * r) / (T**2)
    M = 349.8  # grams

    columns = ["r (m)", "t_1", "t_2", "t_3", "<t> (s)", "T (s)", "a (m/s^2)"]

    data = np.hstack((r, T_all, T_avg, T, a))
    df = pd.DataFrame(data, columns=columns)  # type: ignore
    print(df)

    g = 9.8

    m_hang = np.array([48.3, 248.3, 348.3, 898.3]).reshape(-1, 1) / 1000  # kg
    F_c = m_hang * g

    mass_columns = ["r (m)", "m_h (kg)", "F_h (N)"]
    mass_data = np.hstack((r, m_hang, F_c))
    mdf = pd.DataFrame(mass_data, columns=mass_columns)  # type: ignore
    print(mdf)

    x = a.reshape(-1)
    y = F_c.reshape(-1)
    m_F, b = np.polyfit(x, y, 1)
    plt.plot(x, m_F * x + b, label=f"Trend Line F_c = {m_F}a_c")
    plt.xlabel(r"a_c")
    plt.ylabel(r"F_c")
    plt.legend()
    plt.title("Uniform Circular Motion Lab")
    plt.show()


if __name__ == "__main__":
    main()
