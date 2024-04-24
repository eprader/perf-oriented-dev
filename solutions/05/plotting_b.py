import json
import sys
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    optimisations = [
        "gcse-after-reload",
        "ipa-cp-clone",
        "loop-interchange",
        "loop-unroll-and-jam",
        "peel-loops",
        "predictive-commoning",
        "split-loops",
        "split-paths",
        "tree-loop-distribution",
        "tree-partial-pre",
        # "unroll-completely-grow-size", NOTE: Not valid for `C`
        "unswitch-loops",
        # "version-loops-for-strides", NOTE: Fails for `npb_bt`
    ]
    # optimisations = ["O0", "O1", "O2", "O3", "Ofast", "Os"]

    commands = ["mmul", "nbody", "qap_chr15c", "delannoy_13", "npb_bt_w", "ssca2_15"]
    optimisation_to_count = {optimisation: 0 for optimisation in optimisations}

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
        for i, tup in enumerate(sorted_mean):
            command_str = tup[0]
            only_command = command_str.split()[0]
            last_part = only_command.split("_")[-1]
            optimisation_to_count[last_part] = optimisation_to_count[last_part] + i
        best_performing = [command[0] for command in sorted_mean[:1]]
        print(best_performing)

    smallest_keys = sorted(optimisation_to_count.items(), key=lambda item: item[1])[:3]
    smallest_keys = [item[0] for item in smallest_keys]
    print(optimisation_to_count)
    print(smallest_keys)
