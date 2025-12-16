#!/bin/python

import math


def squared_distance(junction_a, junction_b):
    return (
        (junction_a[0] - junction_b[0]) ** 2
        + (junction_a[1] - junction_b[1]) ** 2
        + (junction_a[2] - junction_b[2]) ** 2
    )


with open("8.txt", "r") as input_file:
    junctions = [
        tuple(map(int, line.rstrip().split(","))) for line in input_file.readlines()
    ]
closest_pair = None
closest_pair_distance = math.inf
sorted_junctions = []
for i in range(len(junctions) - 1):
    for j in range(i + 1, len(junctions), 1):
        pair = (junctions[i], junctions[j])
        distance = squared_distance(*pair)
        sorted_junctions.append((pair, distance))
sorted_junctions.sort(key=lambda junction_pair: junction_pair[1])
circuits = []
for junction_pair in sorted_junctions:
    pair, _ = junction_pair
    existing_circuits = list(
        filter(lambda circuit: any(junction in circuit for junction in pair), circuits)
    )
    if not existing_circuits:
        circuits.append(set(pair))
    elif len(existing_circuits) == 1:
        existing_circuits[0].update(pair)
    else:
        circuits.remove(existing_circuits[1])
        existing_circuits[0].update(existing_circuits[1])
    if len(circuits[0]) == len(junctions):
        print(f"answer: {pair[0][0] * pair[1][0]}")
        break
