import pandas as pd
import numpy as np


def main():
    g_standard = 9.81

    # heights in meters
    heights = np.array([0.63, 0.38, 0.49, 0.71, 0.80])

    # light ball times (s)
    light_times = np.array(
        [
            [0.3531, 0.3517, 0.3574, 0.3488, 0.3459],
            [0.2819, 0.2728, 0.2784, 0.2761, 0.2810],
            [0.3160, 0.3137, 0.3119, 0.3173, 0.3142],
            [0.3825, 0.3752, 0.3777, 0.3648, 0.3925],
            [0.4008, 0.4025, 0.4078, 0.4031, 0.4090],
        ]
    )

    # heavy ball times (s)
    heavy_times = np.array(
        [
            [0.3443, 0.3466, 0.3453, 0.3435, 0.3441],
            [0.2793, 0.2823, 0.2702, 0.2743, 0.2714],
            [0.3089, 0.3046, 0.3138, 0.3034, 0.3039],
            [0.3777, 0.3838, 0.3779, 0.3804, 0.3697],
            [0.3947, 0.3963, 0.3949, 0.4038, 0.3901],
        ]
    )

    balls = {"light": light_times, "heavy": heavy_times}

    results = {}
    for name, times_matrix in balls.items():
        # g values for each datapoint
        g_vals = 2 * heights[:, None] / (times_matrix**2)
        g_df = pd.DataFrame(
            g_vals,
            index=heights,
            columns=[f"trial_{i+1}" for i in range(times_matrix.shape[1])],
        )

        # flatten all 25 values
        g_all = g_df.values.flatten()

        avg_g = np.mean(g_all)
        avg_g2 = np.mean(g_all**2)
        variance = avg_g2 - avg_g**2
        stdev = np.sqrt(variance)
        rel_uncertainty = stdev / avg_g * 100
        percent_diff = (avg_g - g_standard) / g_standard * 100

        stats = {
            "<g>": avg_g,
            "<g^2>": avg_g2,
            "Variance": variance,
            "StdDev": stdev,
            "Rel_Unc": rel_uncertainty,
            "%Diff": percent_diff,
        }

        print(f"\n%%%% {name.upper()} BALL RESULTS %%%%")
        print("Raw g values:\n", g_df)
        print("\nGlobal stats (all 25 trials):")
        for k, v in stats.items():
            print(f"{k}: {v:.5f}")

        results[name] = (g_df, stats)

    return results


if __name__ == "__main__":
    main()
