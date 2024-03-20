## 1
Compile the small_samples and tools before running benchmark.py.
copy this folder into the root of the perf-oriented-dev dir and run the `benchmark.py`.
It is currently set up to run on lcc so it will try to dispatch a slurm job.

A python script `benchmark.py` was created to measure the runtime.
It executes each program 6 times and then calculates the confidence interval.

For my local experiment there was no program that was executed more than 6 times.
Running on lcc was not possible because of some json parse error that I could not get to debug...

Running on lcc resulted in the .json for the first iterations of mmul but not any confidence interval analysis as it
seemed to have trouble with the parsing of the json...
From the limited runs for mmul I could see that it was not significantly impacted by injecting cpu load...
Similar to the local experiment

qap_chr15.json: Mean Execution Time = 1.9249999999999998
qap_chr15_load.json: Mean Execution Time = 2.3833333333333333

mmul.json: Mean Execution Time = 1.7783333333333333
mmul_load.json: Mean Execution Time = 1.7666666666666664

delannoy.json: Mean Execution Time = 0.16333333333333336
delannoy_load.json: Mean Execution Time = 0.15833333333333335

filegen.json: Mean Execution Time = 0.5916666666666667
filegen_load.json: Mean Execution Time = 1.2083333333333333

nbody.json: Mean Execution Time = 0.56
nbody_load.json: Mean Execution Time = 0.56
