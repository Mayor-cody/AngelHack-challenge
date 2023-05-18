def print_layout(layout):
    for row in layout:
        print(''.join(row))
    print()


def calculate_lifeform_score(layout):
    score = 0
    for row in range(5):
        for col in range(5):
            if layout[row][col] == 'X':
                tile_number = row * 5 + col
                score += 2 ** tile_number
    return score


def get_adjacent_lifeforms(layout, row, col):
    lifeforms_count = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        adjacent_row, adjacent_col = row + dx, col + dy
        if 0 <= adjacent_row < 5 and 0 <= adjacent_col < 5 and layout[adjacent_row][adjacent_col] == 'X':
            lifeforms_count += 1
    return lifeforms_count


def next_minute_layout(layout):
    new_layout = [['.'] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            lifeforms_count = get_adjacent_lifeforms(layout, row, col)
            if layout[row][col] == 'X':
                if lifeforms_count == 1:
                    new_layout[row][col] = 'X'
            else:
                if lifeforms_count in (1, 2):
                    new_layout[row][col] = 'X'
    return new_layout


start_state = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X'],
]

print("Start state:")
print_layout(start_state)

encountered_layouts = [start_state]
minute = 1

while True:
    next_layout = next_minute_layout(encountered_layouts[-1])

    if next_layout in encountered_layouts:
        repeated_minute = encountered_layouts.index(next_layout)
        print(
            f"\nRepeated layout: {repeated_minute} minute(s) and {minute} minute(s).")
        break
    else:
        encountered_layouts.append(next_layout)
        minute += 1

lifeform_score = calculate_lifeform_score(encountered_layouts[repeated_minute])
print(f"Lifeform score: {lifeform_score}")
