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

Observations: 
 - `matmul_sub` consistently takes a lot of runtime due to its high number of invocations.
 - Looking at the `matmul_sub` call tree, it is a child function of `x_solve, y_solve, z_solve`
   which all take up a lot of runtime aswell.
 - `compute_rhs`, `set_constants` and `binvcrhs` all have very short running times but are called a substantial
   amount of times.

Comparison:
 - The local output of `gprof` appears to have more functions tracked compared to the `lcc`.
 - The percentages for the functions vary significantly between executions as well as platform.
   The Variation might be due to the sampling interval that `gprof` has on the `lcc` compared to local.

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
| LCC: |------------|----------|------------|---------|---------|-------------|
| 37.50     | 0.03                | 0.03                | 201300| 0.15                | 0.15                | binvcrhs      |
| 25.00     | 0.05                | 0.02                | 61    | 327.91              | 546.52              | z_solve       |
| 12.50     | 0.06                | 0.01                | 201300| 0.05                | 0.05                | matmul_sub    |
| 12.50     | 0.07                | 0.01                | 61    | 163.96              | 382.56              | x_solve       |
| 12.50     | 0.08                | 0.01                | 61    | 163.96              | 382.56              | y_solve       |
| 0.00      | 0.08                | 0.00                | 201300| 0.00  


### a
Local:
| time  | cumulative seconds | self seconds | calls      | self ms/call | total ms/call | name        |
|-------|------------|----------|------------|---------|---------|-------------|
| 28.22  | 41.43           | 41.43     | 6030000 | 0.01            | 0.01           | binvcrhs     |
| 14.68  | 62.98           | 21.55     | 609030000 | 0.00          | 0.00           | matmul_sub  |
| 13.14  | 82.27           | 19.29     | 201     | 95.97           | 218.29         | y_solve      |
| 11.02  | 98.45           | 16.18     |         |                 |                | z_solve      |
| 10.99  | 114.58          | 16.13     | 201     | 80.25           | 202.57         | x_solve      |
| 9.90   | 129.12          | 14.54     | 203     | 71.63           | 71.63          | compute_rhs  |
| LCC: |------------|----------|------------|---------|---------|-------------|
| 30.01     | 21.39               | 21.39               | 146029716| 0.00                | 0.00                | binvcrhs      |
| 18.43     | 34.53               | 13.14               | 146029716| 0.00                | 0.00                | matmul_sub    |
| 13.05     | 43.84               | 9.30                | 201      | 46.27               | 110.65              | y_solve       |
| 11.76     | 52.22               | 8.38                | 201      | 41.70               | 106.07              | z_solve       |
| 10.91     | 60.00               | 7.78                | 201      | 38.71               | 103.08              | x_solve       |
| 9.08      | 66.47               | 6.47                | 202      | 32.03               | 32.03               | compute_rhs   |

### c
Local:
| time  | cumulative seconds | self seconds | calls      | self ms/call | total ms/call | name        |
|-------|------------|----------|------------|---------|---------|-------------|
| 30.87  | 192.24          | 192.24    | 2485324800 | 0.00            | 0.00           | binvcrhs     |
| 15.14  | 286.50          | 94.26     | 2485324800 | 0.00            | 0.00           | matmul_sub  |
| 13.21  | 368.76          | 82.26     | 201       | 0.41            | 0.94           | z_solve      |
| 12.71  | 447.92          | 79.16     | 201       | 0.39            | 0.92           | y_solve      |
| 11.01  | 516.49          | 68.57     | 202       | 0.34            | 0.34           | compute_rhs  |
| LCC: |------------|----------|------------|---------|---------|-------------|
| 30.10     | 368.51              | 368.51              | 2485324800 | 0.00                | 0.00                | binvcrhs      |
| 18.18     | 591.01              | 222.50              | 2485324800 | 0.00                | 0.00                | matmul_sub    |
| 12.94     | 749.37              | 158.36              | 201        | 0.79                | 1.87                | y_solve       |
| 12.93     | 907.68              | 158.31              | 201        | 0.79                | 1.87                | z_solve       |
| 11.02     | 1042.54             | 134.86              | 201        | 0.67                | 1.75                | x_solve       |
| 9.02      | 1152.97             | 110.43              | 202        | 0.55    10.96  | 584.73          | 68.24     | 201       | 0.34            | 0.87           | x_solve      |
