import json
import os
import time

from confidence_interval import confidence_interval
from Profiler import Profiler
from SlurmJob import SlurmJob
from TimeProfiler import TimeProflier

if __name__ == "__main__":
    build_dir: str = "../small_samples/build/"
    commands: list = [
        (
            build_dir + "mmul",
            "lcc_mmul",
        ),
        (
            build_dir + "delannoy 12",
            "lcc_delannoy",
        ),
        (
            build_dir + "nbody",
            "lcc_nbody",
        ),
        (
            build_dir + "filegen 20 5 1024 1048576",
            "lcc_filegen",
        ),
        (
            build_dir + "qap ../small_samples/qap/problems/chr15a.dat",
            "lcc_qap_chr15",
        ),
    ]

    for command in commands:
        command_name: str = command[1]

        profiler: Profiler = TimeProflier(
            command[0],
            command_name,
            6,
            "/bin/time",
        )

        profiles = []
        threshold = 0.1
        file_path = f"./{command_name}.json"

        # HACK: Store profiler script because otherwise it can't be easily passed to
        # the heavy load command.
        script_name = "profiler_command.sh"
        with open(script_name, "w") as sh_file:
            sh_file.write("#!/usr/bin/env bash\n")
            sh_file.write(profiler.get_bash_script())

        os.chmod(script_name, 0o755)

        heavy_load_command: str = (
            "../tools/load_generator/exec_with_workstation_heavy.sh "
        )

        for _ in range(20):
            if os.path.exists(file_path):
                os.remove(file_path)

            job: SlurmJob = SlurmJob(
                command_name,
                command_name,
                profiler,
                f"{heavy_load_command} ./{script_name}",
            )
            job.dispatch()

            # os.system(f"./{script_name}")

            # HACK: Busy wait for job to finish
            while not os.path.exists(file_path):
                time.sleep(1)

            with open(file_path, "r") as file:
                profiles.extend(json.load(file))

            if os.path.exists(file_path):
                os.remove(file_path)

            # NOTE: stop execution if confidence interval was reached
            lower_bound, upper_bound = confidence_interval(
                [float(profile["elapsed_wall_clock_time"]) for profile in profiles],
                confidence=0.99,
            )
            interval_width = upper_bound - lower_bound
            print(f"Confidence Interval (99%): {lower_bound:.6f} - {upper_bound:.6f}")
            if interval_width <= threshold:
                print("Confidence interval width reached the threshold.")
                break

        # HACK: Remove stored job script
        os.remove(script_name)
        # Store all profiles into the JSON file at the end
        with open(file_path, "w") as file:
            json.dump(profiles, file)
