# Define the runners
runners = [
    {'name': 'John', 'speed': 10, 'run_time': 6, 'rest_time': 20},
    {'name': 'James', 'speed': 8, 'run_time': 8, 'rest_time': 25},
    {'name': 'Jenna', 'speed': 12, 'run_time': 5, 'rest_time': 16},
    {'name': 'Josh', 'speed': 7, 'run_time': 7, 'rest_time': 23},
    {'name': 'Jacob', 'speed': 9, 'run_time': 4, 'rest_time': 32},
    {'name': 'Jerry', 'speed': 5, 'run_time': 9, 'rest_time': 18},
]

# Initialize each runner's state
for runner in runners:
    runner['position'] = 0
    runner['is_running'] = True
    runner['time_left'] = runner['run_time']

# Simulate the race for 1234 seconds
for t in range(1, 1235):
    # Update each runner's state
    for runner in runners:
        if runner['is_running']:
            runner['position'] += runner['speed']
            runner['time_left'] -= 1
            if runner['time_left'] == 0:
                runner['is_running'] = False
                runner['time_left'] = runner['rest_time']
        else:
            runner['time_left'] -= 1
            if runner['time_left'] == 0:
                runner['is_running'] = True
                runner['time_left'] = runner['run_time']

    # Determine the distance of the current leader
    leader_distance = max(runner['position'] for runner in runners)

# Print the distance of the winning runner
print(f"The winning runner covered {leader_distance} meters.")
