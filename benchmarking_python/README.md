Whenever you start working on something create an issue and a pull request so the others know you are already working on it.

TODO: create data analysis script that can read the `.json` files.
TODO: potentially create a general JSON schema that describes the `json` content for any `Profiler` class to adhere to
(right now just output names of `time -v`)

A Profilers (once implemented) command parameter should be as general as possible... potentially there should be a neutral Profiler that can be passed in case one 
only want to run the job without profiling... or allow for the future Profiler parameter of the `Job` class to be optional...
