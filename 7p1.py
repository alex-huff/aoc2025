#!/bin/python

with open("7.txt", "r") as input_file:
    manifold = [
        [chr for chr in line] for line in map(str.rstrip, input_file.readlines())
    ]
num_splits = 0
beams = [manifold[0][i] == "S" for i in range(len(manifold[0]))]
for beam_position in range(len(manifold) - 1):
    new_beams = [False for _ in range(len(beams))]
    for i, is_beam in enumerate(beams):
        if not is_beam:
            continue
        if manifold[beam_position + 1][i] == "^":
            new_beams[i - 1] = True
            new_beams[i + 1] = True
            num_splits += 1
        else:
            new_beams[i] = True
    beams[:] = new_beams
print(f"answer: {num_splits}")
