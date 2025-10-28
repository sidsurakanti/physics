import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def main():
    light_l_m = np.array([30.5, 36.5, 43.7, 51.7, 58.2, 69.7, 71.8]) / 100
    heavy_l_m = np.array([36.1, 37.7, 47.4, 55.4, 61.9, 68.8, 76.7]) / 100

    times_d = np.array(
        [
            [
                1.1227,
                1.1212,
                1.1206,
                1.1171,
                1.1178,
                1.1152,
                1.1155,
                1.1132,
                1.1145,
                1.1141,
            ],
            [
                1.2051,
                1.2047,
                1.2042,
                1.2033,
                1.2031,
                1.2023,
                1.2042,
                1.2015,
                1.2009,
                1.2010,
            ],
            [
                1.3312,
                1.3308,
                1.3305,
                1.3247,
                1.3299,
                1.3296,
                1.3287,
                1.3287,
                1.3298,
                1.3273,
            ],
            [
                1.4456,
                1.4445,
                1.4436,
                1.4423,
                1.4437,
                1.4438,
                1.4422,
                1.4430,
                1.4403,
                1.4384,
            ],
            [
                1.5267,
                1.5266,
                1.5283,
                1.5243,
                1.5280,
                1.5236,
                1.5262,
                1.5283,
                1.5234,
                1.5247,
            ],
            [
                1.6180,
                1.6191,
                1.6183,
                1.6165,
                1.6171,
                1.6150,
                1.6162,
                1.632,
                1.6142,
                1.6147,
            ],
            [
                1.7045,
                1.7032,
                1.07027,
                1.7025,
                1.7014,
                1.7031,
                1.7016,
                1.7004,
                1.6966,
                1.7004,
            ],
        ]
    )

    heavy_times_d = np.array(
        [
            [
                1.0987,
                1.0987,
                1.0983,
                1.0981,
                1.0974,
                1.0979,
                1.0974,
                1.0974,
                1.0970,
                1.0971,
            ],
            [
                1.2378,
                1.2361,
                1.2377,
                1.2374,
                1.2371,
                1.2364,
                1.2370,
                1.2365,
                1.2364,
                1.2361,
            ],
            [
                1.3911,
                1.3846,
                1.3861,
                1.3413,
                1.3901,
                1.3847,
                1.3884,
                1.3881,
                1.3882,
                1.3886,
            ],
            [
                1.5025,
                1.0515,
                1.023,
                1.5015,
                1.5018,
                1.5016,
                1.5018,
                1.0510,
                1.5011,
                1.5006,
            ],
            [
                1.5837,
                1.5832,
                1.5837,
                1.5830,
                1.5834,
                1.5828,
                1.5230,
                1.5733,
                1.5784,
                1.5827,
            ],
            [
                1.6713,
                1.6717,
                1.670,
                1.6718,
                1.6711,
                1.6719,
                1.6718,
                1.6707,
                1.6713,
                1.6712,
            ],
            [
                1.7603,
                1.7623,
                1.7611,
                1.7612,
                1.7627,
                1.7619,
                1.762,
                1.7617,
                1.7616,
                1.7629,
            ],
        ]
    )

    data_df = pd.DataFrame(times_d, index=light_l_m)  # type: ignore
    heavy_data_df = pd.DataFrame(heavy_times_d, index=heavy_l_m)  # type: ignore
    print("%%%%%%% LIGHT RAW DATA %%%%%%%%%\n", data_df)
    print("\n%%%%%%% HEAVY RAW DATA %%%%%%%%%\n", heavy_data_df)

    avg_t_light = np.mean(times_d, axis=1)
    avg_t_heavy = np.mean(heavy_times_d, axis=1)

    g_light = []
    for L, row in zip(light_l_m, times_d):
        t = np.mean(row)
        g_light.append(4 * (3.14**2) * L / (t**2))

    g_heavy = []
    for L, row in zip(heavy_l_m, heavy_times_d):
        t = np.mean(row)
        g_heavy.append(4 * (3.14**2) * L / (t**2))

    light_results_d = np.hstack(
        (
            np.array(light_l_m).reshape(-1, 1),
            times_d,
            avg_t_light.reshape(-1, 1),
            np.array(g_light).reshape(-1, 1),
        )
    )

    heavy_results_d = np.hstack(
        (
            np.array(heavy_l_m).reshape(-1, 1),
            heavy_times_d,
            avg_t_heavy.reshape(-1, 1),
            np.array(g_heavy).reshape(-1, 1),
        )
    )

    columns = [
        "Length (m)",
        "T_1 (s)",
        "T_2 (s)",
        "T_3 (s)",
        "T_4 (s)",
        "T_5 (s)",
        "T_6 (s)",
        "T_7 (s)",
        "T_8 (s)",
        "T_9 (s)",
        "T_10 (s)",
        "Avg Time (s)",
        "g (m/s^2)",
    ]

    light_results_df = pd.DataFrame(
        light_results_d,
        columns=columns,  # type: ignore
    )

    heavy_results_df = pd.DataFrame(
        heavy_results_d,
        columns=columns,  # type: ignore
    )

    print("\n%%%%% LIGHT RESULTS %%%%%")
    print(light_results_df.to_string(index=False))
    print("\n%%%%% HEAVY RESULTS %%%%%")
    print(heavy_results_df.to_string(index=False))

    # (T^2, 4pi^2 * l)
    light_T_sq = light_results_df["Avg Time (s)"] ** 2

    light_four_pi2_l = 4 * (3.14**2) * (light_results_df["Length (m)"])
    heavy_T_sq = heavy_results_df["Avg Time (s)"] ** 2
    heavy_four_pi2_l = 4 * (3.14**2) * (heavy_results_df["Length (m)"])

    x, y = light_T_sq, light_four_pi2_l
    x2, y2 = heavy_T_sq, heavy_four_pi2_l

    m, b = np.polyfit(x, y, 1)
    m2, b2 = np.polyfit(x2, y2, 1)

    plt.scatter(
        x,
        y,
        marker="o",
        color="blue",
        label="Light Pendulum Data",
    )
    plt.scatter(
        x2,
        y2,
        marker="x",
        color="orange",
        label="Heavy Pendulum Data",
    )

    plt.plot(
        x,
        m * x + b,
        label=f"Trend line: y = {m:.3f}x + {b:.3f}",
        color="blue",
    )
    plt.plot(
        x2,
        m2 * x2 + b2,
        color="orange",
        label=f"Trend line: y = {m2:.3f}x + {b2:.3f}",
    )
    plt.xlabel(r"$T^2$ (s)")
    plt.ylabel(r"$4\pi^2 l$ (m)")
    plt.legend()
    plt.title(f"Pendulum Experiment Results (m_light={m:.3f}, m_heavy={m2:.3f})")
    plt.show()

    print("Estimated g (light):", m)
    print("Estimated g (heavy):", m2)


if __name__ == "__main__":
    main()
