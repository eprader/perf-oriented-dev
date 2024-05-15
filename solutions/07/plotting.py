from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

plt.xlabel("allocators")
plt.ylabel("User time (s)")
plt.title("User Times in Seconds")
runtimes = [359]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("default", mean_runtime)
plt.errorbar(
    "default",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
runtimes = [647.81, 653.23, 643.34, 646.95]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("rpmalloc", mean_runtime)
plt.errorbar(
    "rpmalloc",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
runtimes = [614.61, 626.94, 646.95, 658.94]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("mimalloc", mean_runtime)
plt.errorbar(
    "mimalloc",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
plt.savefig(f"runtimes.png")

# WALL

plt.figure()
plt.xlabel("allocators")
plt.ylabel("Wall Clock Time (s)")
plt.title("Total Runtime")
runtimes = [350]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("default", mean_runtime)
plt.errorbar(
    "default",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
runtimes = [113.89, 114.15, 108.74, 104.04]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("rpmalloc", mean_runtime)
plt.errorbar(
    "rpmalloc",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
runtimes = [78.28, 108.65, 116.66, 106.87]
mean_runtime: np.floating = np.mean(runtimes)

plt.bar("mimalloc", mean_runtime)
plt.errorbar(
    "mimalloc",
    mean_runtime,
    np.std(runtimes),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
plt.savefig(f"wall_time.png")

# MEM

plt.figure()
plt.xlabel("allocators")
plt.ylabel("Memory usage (kbyte)")
plt.title("Total Memory usage")
memory = [588712]
mean_memory: np.floating = np.mean(memory)

plt.bar("default", mean_memory)
plt.errorbar(
    "default",
    mean_memory,
    np.std(memory),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
memory = [588460, 588740, 590460, 586520]
mean_memory: np.floating = np.mean(memory)

plt.bar("rpmalloc", mean_memory)
plt.errorbar(
    "rpmalloc",
    mean_memory,
    np.std(memory),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
memory = [586280, 587952, 587360, 588664]
mean_memory: np.floating = np.mean(memory)

plt.bar("mimalloc", mean_memory)
plt.errorbar(
    "mimalloc",
    mean_memory,
    np.std(memory),
    fmt=".",
    color="Black",
    capthick=4,
    errorevery=1,
)
plt.savefig(f"memory.png")
