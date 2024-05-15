# Exercise 1
For rpmalloc I needed to remove the -Weverything flag in the `build.ninja` file.
Then follow the README.

For mimalloc:
```bash
mkdir -p out/release
cd out/release
cmake ../..
make
```

To build allscale, make sure you change into the build directory before attempting to do anything.
```bash
git clone https://github.com/allscale/allscale_api.git
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -G Ninja ../code
```

## Default allocator

```
/bin/time -v ninja
```

cpu 5:50
wall 5:59 m
588712 kbyte

following runs were almost identical therefore there are no multitude of runs performed here.


## rpmalloc
```bash
LDD_PRELOAD=../../rpmalloc/bin/linux/release/x86-64/librpmalloc.so /bin/time -v ninja
```

make sure that all `allscale_api` and `rpcmalloc` are in the same folder.

Noticeable difference apart from the runtime: First roughly 90 stages of the build are much faster than with the original allocator.

User time: 647.81s
Wall: 1:53.89
memory: 588460 kbyte

User time: 653.23
Wall: 1:54.15
memory: 588740

User time: 643.34
Wall: 1:48.74
memory: 590460

User time: 635.74
Wall: 1:44.04
memory: 586520

## mimalloc
```bash
LDD_PRELOAD=../../mimalloc/out/release/libmimalloc.so /bin/time -v ninja
```

User time: 614.61
Wall: 1:18.28
memory 586280 kbyte

User time: 626.94
Wall: 1:48.65
memory 587952 kbyte

User time: 646.95
Wall: 1:56.66
memory: 587360

User time: 658.94
Wall: 1:46.87
memory: 588664


# Review
[user](./runtimes.png)
[wall](./wall_time.png)
[memory](./memory.png)

The optimized allocators had more than 100% cpu usage. This would suggest multithreading of the allocator?
User time was also higher meaning more CPU utilization overall.

Memory usage was more or less the same with a bit more variance for the specialized allocators
