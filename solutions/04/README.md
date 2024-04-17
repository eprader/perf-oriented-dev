To build the `larger_samples` use the following command in the folders `larger_samples/npb_bt` and `larger_samples/ssca2`:

```bash
mkdir build
cd build
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_FLAGS="-pg" -DCMAKE_CXX_FLAGS="-pg"
ninja
```


# A)
To run a program using `massif` use `valgrind --tool=massif <program-to-profile>`
All runtimes were averaged over 5 runs.

## ssca2

`ssca2 17` had a normal runtime of ~38.5s.

With `massif` this was ~89.922s.
- 90.328s
- 90.699s
- 89.837s
- 89.246s
- 89.498s

Resulting in a runtime ~233% of to the original.
Perturbation is ~51.422s which is ~133% of the original runtime.

Peak allocators according to the `Allocators` tab are:
- `genScaleData` with a peak of `4.0 MiB`
- `computeGraph` with a peak of `4.0 MiB`
- `betweennessCentrality` with a peak of `4.0 MiB`


## npb_bt

`npb_bt_a` had a regular runtime of ~38.502s
- 38.608s
- 38.627s
- 38.427s
- 38.272s
- 38.576s


With `massif` this was ~537.435s.
- 537.547
- 537.375
- 537.432
- 537.522
- 537.302

Runtime is ~1395% of the original.
Perturbation is ~498.933s which is ~1295% of the original runtime.

Peak allocator for this application is `_IO_file_doallocate` with `1.0 KiB`.


Strange to see that less memory allocated still resulted in such a huge perturbation....
Probably the runtime that `valgrind` simulates also impacts other parts of the program.
In my previous experience `valgrind` has used a lot more runtime, so this is not surprising.
But the relation to the actual runtime is very strange.

# B)
