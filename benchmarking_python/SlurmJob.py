import os

from Profiler import Profiler


class SlurmJob:
    """
    This class creates and disbatches a slurm job running the time command with the given parameters.


    """

    def __init__(
        self, job_name: str, output_log: str, profiler: Profiler, shell_command=None
    ):
        self.job_script: str = (
            "#!/bin/bash\n"
            "# SBATCH --partition=lva\n"
            f"# SBATCH --job-name={job_name}\n"
            f"# SBATCH --output={output_log}.log\n"
            "# SBATCH --ntasks=1\n"
            "# SBATCH --ntasks-per-node=1\n"
            "# SBATCH --exclusive\n"
        )
        self.job_script_name = job_name + ".sh"

        if shell_command:
            self.job_script = self.job_script + shell_command + "\n"
        else:
            self.job_script = self.job_script + profiler.get_bash_script()

    def dispatch(self):
        # store job.sh
        with open(self.job_script_name, "w") as file:
            file.write(self.job_script)
        os.system(f"sbatch ./{self.job_script_name}")
        # print(self.job_script)
