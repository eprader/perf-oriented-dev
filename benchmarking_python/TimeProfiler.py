import json

from Profiler import Profiler


class TimeProflier(Profiler):
    TIME_FORMAT_DICT: dict[str, str] = {
        "command": "%C",
        "user_time_seconds": "%U",
        "system_time_seconds": "%S",
        "percent_of_cpu": "%P",
        "elapsed_wall_clock_time": "%e",
        "maximum_resident_set_size_kbytes": "%M",
        "major_requiring_io_page_faults": "%R",
        "minor_reclaiming_a_frame_page_faults": "%r",
        "voluntary_context_switches": "%w",
        "involuntary_context_switches": "%c",
        "exit_status": "%x",
    }
    TIME_FORMAT_STR: str = json.dumps(TIME_FORMAT_DICT, indent=4)

    def __init__(
        self,
        command: str,
        output_json: str,
        repetitions: int,
        time_command: str = "/bin/time",
    ):
        """
        Initializes the MyProfiler object.

        Args:
            command (str): The command to be profiled.
            output_json (str): The name of the output JSON file. Will append `.json`.
            repetitions (int): The number of repetitions for running the command. Must be >= 0.
        """
        if repetitions < 0:
            raise ValueError("`repetitions` must be >= 0")

        super().__init__(command, output_json)
        self.repetitions = repetitions
        self.time_command = time_command

    def get_bash_script(self):
        """
        Builds a bash script string to be embedded into the slurm job.
        """

        profile_command: str = f"{self.time_command} -f '{self.TIME_FORMAT_STR}' -a -o {self.output_json} {self.command}\n"

        bash_script = f"echo '[' >> {self.output_json}\n" + profile_command

        # NOTE: Loop is only needed if more than 1 `repetitions`
        if self.repetitions > 1:
            bash_script += (
                f"for i in $(seq 2 {self.repetitions}); do\n"
                f"    echo ',' >> {self.output_json}\n"
                + "    "
                + profile_command
                + "done\n"
            )

        bash_script += f"echo ']' >> {self.output_json}"

        return bash_script
