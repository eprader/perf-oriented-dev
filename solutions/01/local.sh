#!/usr/bin/env bash

commands=(
    "../build/delannoy 15"
    "../build/filegen 100 150 1024 1048576"
    "../build/mmul"
    "../build/nbody"
    "../build/qap"
)

for command in "${commands[@]}"; do
    # prepend `sbatch -o "$command.txt"` on lcc3
    sh ./run_n_mean_variance.sh "$command" 4
done

# prepend `sbatch -o "$command.txt"` on lcc3
../build/filegen 100 150 1024 1048576; sh ./run_n_mean_variance.sh ../build/filesearch 4

