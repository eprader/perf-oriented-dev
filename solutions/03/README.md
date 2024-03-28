To build the `larger_samples` use the following command in the `larger_samples/npb_bt` folder:

```bash
mkdir build
cd build
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_FLAGS="-pg" -DCMAKE_CXX_FLAGS="-pg"
ninja
```

# Exercise 1

To use `gprof` locally:
 1. be in the `build` folder

On a local machine run the job.sh. e.g `bash job.sh`.
On the `lcc` use `sbatch job.sh`.

## Local
### s
| time  | cumulative seconds | self seconds | calls      | self ms/call | total ms/call | name        |
|-------|------------|----------|------------|---------|---------|-------------|
| 23.69 | 147.52     | 147.52   | 4970649601 | 0.00    | 0.00    | compute_rhs |
| 15.84 | 246.18     | 98.66    |            |         |         | matmul_sub  |
| 13.71 | 331.53     | 85.35    | 201        | 424.63  | 861.89  | y_solve     |
| 13.24 | 413.99     | 82.46    | 201        | 410.25  | 847.51  | x_solve     |
| 13.23 | 496.41     | 82.42    | 2485324800 | 0.00    | 0.00    | set_constants |
| 6.66  | 537.87     | 41.46    |            |         |         | z_solve     |
| 3.55  | 559.95     | 22.08    | 15436803   | 0.00    | 0.00    | binvcrhs    |

