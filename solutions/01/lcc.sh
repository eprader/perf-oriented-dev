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
    sbatch -o "$command.txt" <<EOF
#!/bin/bash

# Execute job in the partition "lva" unless you have special requirements.
#SBATCH --partition=lva
# Name your job to be able to identify it later
#SBATCH --job-name=test
# Redirect output stream to this file
#SBATCH --output=output.log
# Maximum number of tasks (=processes) to start in total
#SBATCH --ntasks=1
# Maximum number of tasks (=processes) to start per node
#SBATCH --ntasks-per-node=1
# Enforce exclusive node allocation, do not share with other jobs
#SBATCH --exclusive
sh ./run_n_mean_variance.sh "$command" 4
EOF
done

# prepend `sbatch -o "$command.txt"` on lcc3
sbatch -o "filegen.txt" <<EOF
#!/bin/bash

# Execute job in the partition "lva" unless you have special requirements.
#SBATCH --partition=lva
# Name your job to be able to identify it later
#SBATCH --job-name=test
# Redirect output stream to this file
#SBATCH --output=output.log
# Maximum number of tasks (=processes) to start in total
#SBATCH --ntasks=1
# Maximum number of tasks (=processes) to start per node
#SBATCH --ntasks-per-node=1
# Enforce exclusive node allocation, do not share with other jobs
#SBATCH --exclusive
../build/filegen 100 150 1024 1048576; sh ./run_n_mean_variance.sh ../build/filesearch 4
EOF
