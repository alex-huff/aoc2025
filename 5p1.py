#!/bin/python

with open("5.txt", "r") as input_file:
    ranges_txt, ids_txt = input_file.read().split("\n\n")
ranges = [tuple(map(int, line.rstrip().split("-"))) for line in ranges_txt.split("\n")]
ids = [int(line.rstrip()) for line in ids_txt.split("\n") if line]
num_fresh_ingredients = 0


def in_range(range, id):
    return range[0] <= id <= range[1]


for id in ids:
    try:
        next(filter(lambda range: in_range(range, id), ranges))
        num_fresh_ingredients += 1
    except StopIteration:
        pass
print(f"answer: {num_fresh_ingredients}")
