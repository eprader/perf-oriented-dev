import os

from Profiler import Profiler
from SlurmJob import SlurmJob
from TimeProfiler import TimeProflier

if __name__ == "__main__":
    small_samples_dir: str = "../small_samples/build/"
    commands: list = [
        (
            small_samples_dir + "mmul",
            "mmul",
        ),
        (
            small_samples_dir + "nbody",
            "lcc_nbody",
        ),
        (
            small_samples_dir + "qap ../small_samples/qap/problems/chr15c.dat",
            "lcc_qap_chr15",
        ),
        (
            small_samples_dir + "delannoy 13",
            "delannoy",
        ),
    ]
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

    for command in commands:
        for optimization in optimizations:
            command_name: str = command[1] + "_" + optimization

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
