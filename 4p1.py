#!/bin/python

neighbors = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

with open("4.txt", "r") as input_file:
    grid = list(
        list(char == "@" for char in line.rstrip()) for line in input_file.readlines()
    )


def in_bounds(row, col):
    if row < 0 or col < 0:
        return False
    if row >= len(grid) or col >= len(grid[row]):
        return False
    return True


num_accessable_rolls = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if not grid[row][col]:
            continue
        if (
            sum(
                map(
                    lambda pos: in_bounds(*pos) and grid[pos[0]][pos[1]],
                    ((offset[0] + row, offset[1] + col) for offset in neighbors),
                )
            )
            < 4
        ):
            num_accessable_rolls += 1

print(f"answer: {num_accessable_rolls}")
