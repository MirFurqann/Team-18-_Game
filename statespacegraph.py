def find_xyz_combinations(target_sums):
    # Initialize a dictionary to hold the combinations for each target sum
    combinations = {target_sum: [] for target_sum in target_sums}
    
    # Iterate through possible values of x, y, z
    for x in range(26):
        for y in range(26):
            for z in range(26):
                # Calculate the sum of x, y, z
                current_sum = x + y + z
                # If the sum is one of the target sums, add the combination
                if current_sum in target_sums:
                    combinations[current_sum].append((x, y, z))
                    
    return combinations

# Define the target sums
target_sums = range(15, 26)  # 15 to 25 inclusive

# Get the combinations
xyz_combinations = find_xyz_combinations(target_sums)

# Display the results
for target_sum, combinations in xyz_combinations.items():
    print(f"Sum = {target_sum}: {len(combinations)} combinations")
    print(combinations[:351])

xyz_combinations
