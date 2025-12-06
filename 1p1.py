#!/bin/python

with open("1.txt", "r") as input_file:
    lines = list(map(str.rstrip, input_file.readlines()))
rotations = [(line[0], int(line[1:])) for line in lines]
current_position = 50
num_steps_at_zero = 0
for rotation in rotations:
    direction = -1 if rotation[0] == "L" else 1
    current_position += direction * rotation[1]
    current_position %= 100
    if not current_position:
        num_steps_at_zero += 1
print(f"answer: {num_steps_at_zero}")
