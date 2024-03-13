#!/usr/bin/env bash

calculate_mean() {
    local sum=0
    local count=0
    for time in "${@}"; do
        sum=$(bc <<< "${sum} + ${time}")
        ((count++))
    done
    mean=$(bc <<< "scale=10; ${sum} / ${count}")
    echo "${mean}"
}

calculate_variance() {
    local mean="$1"
    local count=0
    local squared_sum=0
    for time in "${@:2}"; do
        squared_sum=$(bc <<< "${squared_sum} + (${time} - ${mean})^2")
        ((count++))
    done
    variance=$(bc <<< "scale=10; ${squared_sum} / ${count}")
    echo "${variance}"
}

# Main script
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <command> <number_of_times>"
    exit 1
fi

command="$1"
num_times="$2"

times=()

# Create or append to CSV file
csv_file="execution_times.csv"
if [ ! -e "$csv_file" ]; then
    echo "Command,Runtime" > "$csv_file"
fi

for ((i=1; i<=num_times; i++)); do
    start=$(date +%s.%N)

    eval "$command" > /dev/null

    end=$(date +%s.%N)

    elapsed=$(bc <<< "${end} - ${start}")
    times+=("$elapsed")

    echo "\"$command\",$elapsed" >> "$csv_file"
done

mean=$(calculate_mean "${times[@]}")
variance=$(calculate_variance "$mean" "${times[@]}")

echo "Mean execution time: $mean seconds"
echo "Variance: $variance seconds^2"
echo "Execution times stored in: $csv_file"
