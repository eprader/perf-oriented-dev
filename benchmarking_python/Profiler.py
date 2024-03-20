from abc import ABC, abstractmethod


class Profiler(ABC):
    """
    A profiler takes a command as an input and profiles this command.
    The profiler will store the results in a file called `<output_json>.json`.
    """

    def __init__(self, command: str, output_json: str):
        self.command = command
        self.output_json = output_json + ".json"

    @abstractmethod
    def get_bash_script(self) -> str:
        """
        Returns the bash script to be run.
        """
        pass
