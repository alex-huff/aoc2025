#!/bin/python

import math


def squared_distance(junction_a, junction_b):
    return (
        (junction_a[0] - junction_b[0]) ** 2
        + (junction_a[1] - junction_b[1]) ** 2
        + (junction_a[2] - junction_b[2]) ** 2
    )


def junction_in_circuit(junction_pair, circuit):
    return any(junction in circuit for junction in junction_pair)


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
first_1000_junctions = sorted_junctions[:1000]
circuits = []
for junction_pair in first_1000_junctions:
    pair, _ = junction_pair
    existing_circuits = [
        circuit for circuit in circuits if junction_in_circuit(pair, circuit)
    ]
    if not existing_circuits:
        new_set = set()
        new_set.update(pair)
        circuits.append(new_set)
    else:
        existing_circuits[0].update(pair)
        if len(existing_circuits) > 1:
            circuits.remove(existing_circuits[1])
            existing_circuits[0].update(existing_circuits[1])
circuits.sort(key=lambda circuit: len(circuit), reverse=True)
print(f"answer: {eval('*'.join(map(lambda circuit: str(len(circuit)), circuits[:3])))}")
