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
On the `lcc` use `sbatch job.sh` with the provided job script.

