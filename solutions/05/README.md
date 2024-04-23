The `CMakeLists.txt` of `./small_samples` as well as `./larger_samples/npb_bt` and `./larger_samples/ssca2`
were modified to build all optimization levels as separate binaries.

To build, copy the respective files into the source folders of `perf-oriented-dev` and run the following commands:

```bash
mkdir build
cd build
cmake .. -G Ninja
ninja
```

## A)

The `benchmarking-python/benchmarking_a.py` file will run all required programs **5** times and store the results in a `JSON` file.
>[!NOTE]
>The script will also create `.sh` and `.out` files run `rm *.out *.sh` to remove these files.
>The json files need to be moved into a `data` folder for the plotting script to pick them up.
>```bash
>   mkdir data && mv *.json data
>```

To generate all plots run:
```bash
for program in "mmul" "nbody" "qap_chr15c" "delannoy_13" "npb_bt_w" "ssca2_15"
do
    python plotting_a.py $program
done
```

![mmul](./mmul.png)
![nbody](./nbody.png)
![qap_chr15c](./qap_chr15c.png)
![delannoy_13](./delannoy_13.png)
![npb_bt_w](./npb_bt_w.png)
![ssca2_15](./ssca2_15.png)
