import json
import os

directory = "."  # Assuming the files are in the current directory


for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(filename, "r") as file:
            profiles = json.load(file)
            execution_times = [
                float(profile["elapsed_wall_clock_time"]) for profile in profiles
            ]
            mean_elapsed_time = sum(execution_times) / len(execution_times)
            print(f"{filename}: Mean Execution Time = {mean_elapsed_time}")
