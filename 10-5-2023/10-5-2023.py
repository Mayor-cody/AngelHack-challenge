def min_task_cost(efficiency):
    n = len(efficiency)
    min_cost = float('inf')
    for i in range(n):
        remaining = efficiency[:i] + efficiency[i+1:]
        remaining.sort()
        cost = sum([abs(remaining[j] - remaining[j+1])
                   for j in range(0, n-2, 2)])
        min_cost = min(min_cost, cost)
    return min_cost


efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
              123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

print(min_task_cost(efficiency))
