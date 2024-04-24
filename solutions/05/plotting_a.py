import json
import sys
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python plotting_a.py <file_name> (Example: python plotting_a.py qap_chr15c)"
        )
        sys.exit(1)

optimisations = ["O0", "O1", "O2", "O3", "Ofast", "Os"]
file_names = [f"{sys.argv[1]}_{optimisation}" for optimisation in optimisations]
plt.figure()


plt.xlabel("Optimisations")
plt.ylabel("Average Runtime With StD (s)")
plt.title(sys.argv[1])
for optimisation in optimisations:
    file_name = f"{sys.argv[1]}_{optimisation}"
    with open(f"./data/{file_name}.json", "r") as json_file:
        data: List[Dict] = json.load(json_file)

    runtimes: List[float] = [float(d["elapsed_wall_clock_time"]) for d in data]
    mean_runtime: np.floating = np.mean(runtimes)

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
plt.savefig(f"{sys.argv[1]}.png")
