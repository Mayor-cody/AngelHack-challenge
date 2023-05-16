runners = [
    {'name': 'John', 'speed': 10, 'run_time': 6, 'rest_time': 20},
    {'name': 'James', 'speed': 8, 'run_time': 8, 'rest_time': 25},
    {'name': 'Jenna', 'speed': 12, 'run_time': 5, 'rest_time': 16},
    {'name': 'Josh', 'speed': 7, 'run_time': 7, 'rest_time': 23},
    {'name': 'Jacob', 'speed': 9, 'run_time': 4, 'rest_time': 32},
    {'name': 'Jerry', 'speed': 5, 'run_time': 9, 'rest_time': 18}
]

distances = {}

for runner in runners:
    distance = 0
    time = 0
    while time < 1234:
        if time % (runner['run_time'] + runner['rest_time']) < runner['run_time']:
            distance += runner['speed']
        time += 1
    distances[runner['name']] = distance

winner = max(distances, key=distances.get)
winning_distance = distances[winner]

print(f'The winner is {winner} with a distance of {winning_distance} meters in 1234 seconds.')
