import os

from Profiler import Profiler
from SlurmJob import SlurmJob
from TimeProfiler import TimeProflier

if __name__ == "__main__":
    optimizations = [
        "O0",
        # "O1",
        # "O2",
        # "O3",
        # "Ofast",
        # "Os",
        # "fgcse_after_reload",
        # "fpeel_loops",
        # "ftree_loop_distribution",
        # "fversion_loops_for_strides",
        # "fipa_cp_clone",
        # "fpredictive_commoning",
        # "ftree_partial_pre",
        # "floop_interchange",
        # "fsplit_loops",
        # "funswitch_loops",
        # "floop_unroll_and_jam",
        # "fsplit_paths",
        # "fvect_cost_model_dynamic",
    ]

    small_samples_dir: str = "../small_samples/build/"
    commands = (
        [
            (
                small_samples_dir + "mmul_" + optimization,
                "mmul_" + optimization,
            )
            for optimization in optimizations
        ]
        + [
            (
                small_samples_dir + "nbody_" + optimization,
                "nbody_" + optimization,
            )
            for optimization in optimizations
        ]
        + [
            (
                small_samples_dir
                + "qap_"
                + optimization
                + " ../small_samples/qap/problems/chr15c.dat",
                "qap_chr15c_" + optimization,
            )
            for optimization in optimizations
        ]
        + [
            (
                small_samples_dir + "delannoy_" + optimization + " 13",
                "delannoy_" + optimization,
            )
            for optimization in optimizations
        ]
        + [
            (
                "../larger_samples/npb_bt/build/npb_bt_w",
                "npb_bt_w" + optimization,
            )
            for optimization in optimizations
        ]
        + [
            (
                "../larger_samples/ssca2/build/ssca2_" + optimization + "15",
                "npb_bt_w" + optimization,
            )
            for optimization in optimizations
        ]
    )

    for command in commands:
        command_name: str = command[1]

        profiler: Profiler = TimeProflier(
            command[0],
            command_name,
            5,
            "/bin/time",
            # "/run/current-system/sw/bin/time",
        )

        file_path = f"./{command_name}.json"

        if os.path.exists(file_path):
            os.remove(file_path)

        job: SlurmJob = SlurmJob(
            command_name,
            command_name,
            profiler,
        )
        job.dispatch()
