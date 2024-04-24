import json
import sys
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print(
    #         "Usage: python plotting_a.py <file_name> (Example: python plotting_a.py qap_chr15c)"
    #     )
    #     sys.exit(1)

    # optimisations = [
    #     "fgcse-after-reload",
    #     "fipa-cp-clone",
    #     "floop-interchange",
    #     "floop-unroll-and-jam",
    #     "fpeel-loops",
    #     "fpredictive-commoning",
    #     "fsplit-loops",
    #     "fsplit-paths",
    #     "ftree-loop-distribution",
    #     "ftree-partial-pre",
    #     # "funroll-completely-grow-size", NOTE: Not valid for `C`
    #     "funswitch-loops",
    #     # "fversion-loops-for-strides", NOTE: Fails for `npb_bt`
    # ]
    optimisations = ["O0", "O1", "O2", "O3", "Ofast", "Os"]

    commands = ["mmul", "nbody", "qap_chr15c", "delannoy_13", "npb_bt_w", "ssca2_15"]
    for command in commands:
        plt.figure()
        plt.xlabel("Optimisations")
        plt.ylabel("Average Runtime With StD (s)")
        plt.title(command)
        all_means: List[Tuple[str, np.floating]] = []

        for optimisation in optimisations:
            file_name = f"{command}_{optimisation}"
            with open(f"./data/{file_name}.json", "r") as json_file:
                data: List[Dict] = json.load(json_file)

            runtimes: List[float] = [float(d["elapsed_wall_clock_time"]) for d in data]
            mean_runtime: np.floating = np.mean(runtimes)

            all_means.append((data[0]["command"], mean_runtime))

            plt.bar(optimisation, mean_runtime)
            plt.errorbar(
                optimisation,
                mean_runtime,
                np.std(runtimes),
                fmt=".",
                color="Black",
                capthick=4,
                errorevery=1,
            )
        plt.savefig(f"{command}.png")

        sorted_mean = sorted(all_means, key=lambda x: x[1])
        best_perfroming = [command[0] for command in sorted_mean[:1]]
        print(best_perfroming)
