# A) Preparation

To build `small_samples` on lcc3 one needs to first load the modules specified in `/ldcc3_helpers/modules.sh`.

>[!NOTE]
> Adding them to your `.bashrc` might make life easier for the future.

## delannoy
This program calculates the delannoy number for a given grid size n.
Furthermore, it checks the result with a predefined list and is therefore only
able to calculate a limited number of delannoy numbers.
The algorithm is recursive and therefore scales pretty drastically.
For an acceptable runtime that is not too short, to reduce the impact of random system noise I chose `n = 15`

relevant output from `/bin/time -v`:

 User time (seconds): 136.93
System time (seconds): 0.00
Percent of CPU this job got: 99%
Elapsed (wall clock) time (h:mm:ss or m:ss): 2:17.13
Maximum resident set size (kbytes): 1304

This execution time might need to be reduced for `B`.

## filegen
Input parameters are:
`<num_directories> <num_files_per_directory> <min_file_size> <max_file_size> [<seed>]`

The only ones relevant for scaling are the first two as these are the most impactful when scaling the workload.
I chose the following parameters to get a long enough execution time. This might need to be reduces for `B`.

For this initial benchmark I chose 3 and 15
so `./filegen 100 150 1024 1048576`.

User time (seconds): 104.24
System time (seconds): 3.96
Percent of CPU this job got: 87%
Elapsed (wall clock) time (h:mm:ss or m:ss): 2:03.12
Maximum resident set size (kbytes): 2508

## filesearch
This program looks for the largest file starting from the current directory the program is executed in.
Together with the previous `filegen` command one can scale the executio

```bash
/bin/time -v ./filegen 100 150 1024 1048576
/bin/time -v ./filesearch

```
User time (seconds): 0.01
System time (seconds): 0.12
Percent of CPU this job got: 89%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.16
Maximum resident set size (kbytes): 1416

## mmul

Scales with the size of the matrices multiplied.
I modified the source code, but one can also pass `-D S= 2000` override the `#define`.
One can also see very significant memory usage for the matrices.
I chose 2000 because I think this will also be applicable for `B` and is not so short of an execution time.

User time (seconds): 24.05
System time (seconds): 0.02
Percent of CPU this job got: 99%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:24.16
Maximum resident set size (kbytes): 94864

## nbody

This program simulates n particles in space and their gravitational interactions in 3D.
It scales with the number of particles as well as the number of iterations.
Can be changed by compiler directive or with changing the source code.

For this problem I kept the default settings.

User time (seconds): 2.57
System time (seconds): 0.00
Percent of CPU this job got: 99%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:02.58
Maximum resident set size (kbytes): 1860

## qap

This program calculates the solution for a quadratic assignment problem
which it reads from files in the `problems` folder.

It scales with the problem size.
Changed problem file to
```c
char* problem_file = "problems/chr15a.dat";
```
This lead to a not to short execution time that can also be used for `B`.


>[!NOTE]
> The binary needs to be executed from within the `qap` folder as the path is relative.
> e.g `../build/qap`

User time (seconds): 3.48
System time (seconds): 0.00
Percent of CPU this job got: 99%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:03.51
Maximum resident set size (kbytes): 1496


# B) Experiments
The `run_n_mean_variance.sh` script is used to run each binary n times in this case 4.
It will store the execution times in `execution_times.csv`.

Local system specification:

```text
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         48 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  6
  On-line CPU(s) list:   0-5
Vendor ID:               AuthenticAMD
  Model name:            AMD Ryzen 5 4500U with Radeon Graphics
    Thread(s) per core:  1
    Core(s) per socket:  6
    Socket(s):           1
    Frequency boost:     enabled
    CPU(s) scaling MHz:  124%
    CPU max MHz:         2375,0000
    CPU min MHz:         1400,0000
Caches (sum of all):     
  L1d:                   192 KiB (6 instances)
  L1i:                   192 KiB (6 instances)
  L2:                    3 MiB (6 instances)
  L3:                    8 MiB (2 instances)
NUMA:                    
  NUMA node(s):          1
  NUMA node0 CPU(s):     0-5
```

To run the benchmark on a local machine run `local.sh` within the `small_samples/qap` folder.

> [!NOTE] 
> `run_n_mean_variance.sh` needs to be in the same folder as well.

## delannoy
Mean execution time: 54.6976342735 seconds
Variance: .0036329746 seconds^2

Mean execution time: 419.0089523825 seconds
Variance: 20518.3895121736 seconds^2

Mean execution time: 1.1941223612 seconds
Variance: .0001142082 seconds^2

Mean execution time: .5691654300 seconds
Variance: .0000004983 seconds^2

Mean execution time: .0042522652 seconds
Variance: .0000010671 seconds^2

Mean execution time: .1174281897 seconds
Variance: .0266639543 seconds^2
