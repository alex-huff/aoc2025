#!/bin/python

with open("5.txt", "r") as input_file:
    ranges_txt, ids_txt = input_file.read().split("\n\n")
ranges = [list(map(int, line.rstrip().split("-"))) for line in ranges_txt.split("\n")]
ids = [int(line.rstrip()) for line in ids_txt.split("\n") if line]
num_fresh_ingredients = 0
ranges.sort(key=lambda range: range[0])
while len(ranges):
    current_range = ranges[0]
    while len(ranges) > 1 and current_range[0] <= ranges[1][0] <= current_range[1]:
        current_range[1] = max(current_range[1], ranges[1][1])
        del ranges[1]
    num_fresh_ingredients += (current_range[1] - current_range[0]) + 1
    del ranges[0]
print(f"answer: {num_fresh_ingredients}")
