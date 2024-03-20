import os

from Profiler import Profiler
from TimeProfiler import TimeProflier


class SlurmJob:
    # TODO: improve docs
    # TODO : Create Job class that is more general and allows for local execution
    """
    This class creates and disbatches a slurm job running the time command with the given parameters.


    """

    def __init__(
        self, job_name: str, output_log: str, profiler: Profiler, shell_command=None
    ):
        """
        Initializes a SlurmJob object.

        Parameters:
            job_name (str): Name of the job.
            output_log (str): Name of the output log file.
                The provided string will have an added file extension `.log`.
            command (str): Command to be executed by the job.
            output_json (str): Path to the JSON file where the profiling output will be stored.
                The job will only append its time output to this file.
        """
        self.job_script: str = (
            "#!/bin/bash\n"
            "# SBATCH --partition=lva\n"
            f"# SBATCH --job-name={job_name}\n"
            f"# SBATCH --output={output_log}.log\n"
            "# SBATCH --ntasks=1\n"
            "# SBATCH --ntasks-per-node=1\n"
            "# SBATCH --exclusive\n"
        )

        if shell_command:
            self.job_script = self.job_script + shell_command + "\n"
        else:
            self.job_script = self.job_script + profiler.get_bash_script()

    def dispatch(self):
        # TODO: think of the most elegant way to have the file be appended to.
        # e.g Should every `Profiler` class just append to a file path that it gets as a parameter and this disbatch command
        # needs to create this file at the start before calling `sbatch` ?
        # This will allow for multiple runs
        # print(f"sbatch <<EOF\n{self.job_script}\nEOF")
        os.system(f"sbatch <<EOF\n{self.job_script}\nEOF")
