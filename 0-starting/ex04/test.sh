#!/bin/zsh

# Test cases
test_cases=(
    "14"
    "-5"
    ""
    "0"
    "Hi!"
    "13 5"  # Multiple arguments
)
# Path to the whatis.py script
whatis_script="./whatis.py"

# Loop through the test cases
for test_case in "${test_cases[@]}"; do
    echo "Testing: $test_case"
    eval "python3 $whatis_script $test_case"
    echo
done
