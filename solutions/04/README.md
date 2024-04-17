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

[Hardware cache events] of `perf list`

```text
  L1-dcache-load-misses                              [Hardware cache event]
  L1-dcache-loads                                    [Hardware cache event]
  L1-dcache-prefetch-misses                          [Hardware cache event]
  L1-dcache-prefetches                               [Hardware cache event]
  L1-dcache-store-misses                             [Hardware cache event]
  L1-dcache-stores                                   [Hardware cache event]
  L1-icache-load-misses                              [Hardware cache event]
  L1-icache-loads                                    [Hardware cache event]
  LLC-load-misses                                    [Hardware cache event]
  LLC-loads                                          [Hardware cache event]
  LLC-prefetch-misses                                [Hardware cache event]
  LLC-prefetches                                     [Hardware cache event]
  LLC-store-misses                                   [Hardware cache event]
  LLC-stores                                         [Hardware cache event]
  branch-load-misses                                 [Hardware cache event]
  branch-loads                                       [Hardware cache event]
  dTLB-load-misses                                   [Hardware cache event]
  dTLB-loads                                         [Hardware cache event]
  dTLB-store-misses                                  [Hardware cache event]
  dTLB-stores                                        [Hardware cache event]
  iTLB-load-misses                                   [Hardware cache event]
  iTLB-loads                                         [Hardware cache event]
  node-load-misses                                   [Hardware cache event]
  node-loads                                         [Hardware cache event]
  node-prefetch-misses                               [Hardware cache event]
  node-prefetches                                    [Hardware cache event]
  node-store-misses                                  [Hardware cache event]
  node-stores                                        [Hardware cache event]
```

The following results were acquired via `perf stats -e <list-of-events> <command-to-profile>`

For both programs the perturbation was not significant.
The runtimes were the same with some runtime variance for both using `perf` and only running the program itself.

Most significant miss rates:

ssca2:

l1 dcache load, prefetch and store: ~26% ~63% ~11%
LLC load and prefetch: ~10% ~25%
and branch load : ~171%

Not sure how this can be more than 100%?

npb_bt:

LLC load and prefetch: ~52% ~62% -> larger than for ssca2
branch load: 73% (lower) than ssca2


## ssca2 17

 4,308,880,166      L1-dcache-load-misses:u  time: 35.23
16,062,244,597      L1-dcache-loads:u time: 35.41

~26.8% miss rate

   493,175,970      L1-dcache-prefetch-misses:u time: 35.27
   772,201,291      L1-dcache-prefetches:u

~63.8% miss rate

   653,067,751      L1-dcache-store-misses:u                                    
 5,524,724,622      L1-dcache-stores:u                                          

~11.8% miss rate

       313,761      L1-icache-load-misses:u   #    0.00% of all L1-icache accesses
37,522,271,852      L1-icache-loads:u                                           

~ 0.0008% miss rate

   302,406,530      LLC-load-misses:u         #   10.81% of all LL-cache accesses  (49.99%)
 2,797,311,262      LLC-loads:u                                                   (50.01%)

 ~10.8% miss rate

     1,256,439      LLC-prefetch-misses:u                                         (50.01%)
     4,995,203      LLC-prefetches:u                                              (49.99%)

~25.15% miss rate

    44,105,073      LLC-store-misses:u                                            (66.67%)
 1,944,706,780      LLC-stores:u                                                  (66.66%)

~2.26% miss rate

13,235,450,446      branch-load-misses:u                                          (66.67%)
 7,721,559,916      branch-loads:u                                                (66.67%)

~171% miss rate ?????

 1,470,577,119      dTLB-load-misses:u        #    9.16% of all dTLB cache accesses  (66.67%)
16,058,824,970      dTLB-loads:u                                                  (66.67%)

~9.15% miss rate

   286,577,182      dTLB-store-misses:u                                           (66.66%)
 5,524,222,401      dTLB-stores:u                                                 (66.66%)

~5.18% miss rate

       293,614      iTLB-load-misses:u        #    0.00% of all iTLB cache accesses  (66.67%)
45,220,567,253      iTLB-loads:u                                                  (66.67%)

~0.00064% miss rate

            52      node-load-misses:u                                            (66.67%)
   298,697,662      node-loads:u                                                  (66.67%)

 ~0.0%

            21      node-prefetch-misses:u                                        (50.01%)
     1,243,881      node-prefetches:u                                             (50.01%)

~0.0016% miss rate

             0      node-store-misses:u                                           (49.99%)
    39,593,491      node-stores:u                                                 (49.99%)

0% miss rate

 ## npbbt_a

  6,849,092,935      L1-dcache-load-misses:u   #    4.11% of all L1-dcache accesses  (66.67%)
166,477,761,472      L1-dcache-loads:u                                             (66.67%)

~4.11% miss rate

             46      L1-dcache-prefetch-misses:u                                     (66.67%)
              0      L1-dcache-prefetches:u                                        (66.67%)
~100% miss rate ??

  2,425,616,130      L1-dcache-store-misses:u                                      (66.67%)
 79,710,046,792      L1-dcache-stores:u                                            (66.67%)

~3.04% miss rate

    118,807,095      L1-icache-load-misses:u   #    0.08% of all L1-icache accesses
148,028,536,030      L1-icache-loads:u                                           

~0.0802% miss rate

    305,043,373      LLC-load-misses:u         #   52.34% of all LL-cache accesses  (33.33%)
    582,838,212      LLC-loads:u                                                   (33.33%)

~52.33% miss rate

    479,983,112      LLC-prefetch-misses:u                                         (33.33%)
    773,983,700      LLC-prefetches:u                                              (33.33%)

~62.01% miss rate

     26,266,463      LLC-store-misses:u                                            (33.33%)
    444,744,870      LLC-stores:u                                                  (33.33%)

~5.90% miss rate

  4,998,110,227      branch-load-misses:u                                          (66.67%)
  6,766,503,421      branch-loads:u                                                (66.67%)

~73.86% miss rate

      1,272,217      dTLB-load-misses:u        #    0.00% of all dTLB cache accesses  (66.67%)
166,474,833,130      dTLB-loads:u                                                  (66.67%)
~0.0007% miss rate

        336,966      dTLB-store-misses:u                                           (66.67%)
 79,707,538,079      dTLB-stores:u                                                 (66.67%)
~0.00042% miss rate

         17,279      iTLB-load-misses:u        #    0.00% of all iTLB cache accesses
406,463,891,340      iTLB-loads:u                                                
~0.0% miss rate

          1,743      node-load-misses:u                                            (33.33%)
    306,626,248      node-loads:u                                                  (33.33%)
~0.00056% miss rate

          4,580      node-prefetch-misses:u                                        (33.33%)
    478,781,330      node-prefetches:u                                             (33.33%)
~0.00095% miss rate

              0      node-store-misses:u                                           (33.33%)
     27,311,171      node-stores:u                                                 (33.33%)
0% miss rate

