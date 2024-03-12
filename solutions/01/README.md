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

## filegen
Input parameters are:
`<num_directories> <num_files_per_directory> <min_file_size> <max_file_size> [<seed>]`

The only ones relevant for scalin are the first two as these are the most impactful when scaling the workload.

For this initial benchmark I chose 3 and 15
so `./filegen 100 150 1024 1048576`.

User time (seconds): 104.24
System time (seconds): 3.96
Percent of CPU this job got: 87%
Elapsed (wall clock) time (h:mm:ss or m:ss): 2:03.12
Maximum resident set size (kbytes): 2508

## filesearch
This program looks for the largest file starting from the current directory the program is executed in.
Together with the previous `filegen` command one can scale the executiontime.
with 

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
I modified the source code, but one can also pass `-D S= 10000` override the `#define`.
One can also see very significant memory usage for the matrices.

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
char* problem_file = "problems/chr25a.dat";
```


>[!NOTE]
> The binary needs to be executed from within the `qap` folder as the path is relative.
> e.g `../build/qap`
