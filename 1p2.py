#!/bin/python

with open("1.txt", "r") as input_file:
    lines = list(map(str.rstrip, input_file.readlines()))
rotations = [(line[0], int(line[1:])) for line in lines]
current_position = 50
num_clicks_at_zero = 0
dial_size = 100
for rotation in rotations:
    amount = rotation[1]
    direction = -1 if rotation[0] == "L" else 1
    if current_position != 0:
        till_zero = (
            current_position if direction == -1 else (dial_size - current_position)
        )
        if amount < till_zero:
            current_position += direction * amount
            continue
        amount -= till_zero
        num_clicks_at_zero += 1
    num_clicks_at_zero += amount // dial_size
    current_position = direction * amount
    current_position %= dial_size
print(f"answer: {num_clicks_at_zero}")
