#!/bin/python

with open("6.txt", "r") as input_file:
    grid = [line.rstrip().split() for line in input_file.readlines()]
total = sum(
    eval(grid[-1][col].join(grid[i][col] for i in range(len(grid) - 1)))
    for col in range(len(grid[0]))
)
print(f"answer: {total}")
