import itertools

# Generate all permutations of the integer string
perms = itertools.permutations("1867")

# Check each permutation for divisibility by 7
divisible_perms = []
for perm in perms:
    num = int("".join(perm))
    if num % 7 == 0:
        divisible_perms.append(num)

# If there are no divisible permutations, print an error message
if len(divisible_perms) == 0:
    print("No permutations of 1867 are divisible by 7")
else:
    # Calculate the average of the smallest and largest divisible permutations
    smallest = min(divisible_perms)
    largest = max(divisible_perms)
    average = (smallest + largest) / 2

    # Print the result
    print("The smallest divisible permutation is", smallest)
    print("The largest divisible permutation is", largest)
    print("The average of the smallest and largest divisible permutations is", average)
