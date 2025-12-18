#!/bin/python


def area(pos1, pos2):
    return (abs(pos1[0] - pos2[0]) + 1) * (abs(pos1[1] - pos2[1]) + 1)


with open("9.txt", "r") as input_file:
    red_tiles = [
        tuple(map(int, line.split(",")))
        for line in map(str.rstrip, input_file.readlines())
    ]
largest_area = 0
for i in range(len(red_tiles) - 1):
    for j in range(i + 1, len(red_tiles) - 1):
        rectangle_area = area(red_tiles[i], red_tiles[j])
        if rectangle_area > largest_area:
            largest_area = rectangle_area
print(f"answer: {largest_area}")
