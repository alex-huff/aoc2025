#!/bin/python

with open("7.txt", "r") as input_file:
    manifold = [
        [chr for chr in line] for line in map(str.rstrip, input_file.readlines())
    ]
beams = [[False, 0] for i in range(len(manifold[0]))]
beams[manifold[0].index("S")][:] = (True, 1)
for beam_position in range(len(manifold) - 1):
    new_beams = [[False, 0] for _ in range(len(beams))]
    for i, (is_beam, num_timelines) in enumerate(beams):
        if not is_beam:
            continue
        if manifold[beam_position + 1][i] == "^":
            new_beams[i - 1][0] = True
            new_beams[i - 1][1] += num_timelines
            new_beams[i + 1][0] = True
            new_beams[i + 1][1] += num_timelines
        else:
            new_beams[i][0] = True
            new_beams[i][1] += num_timelines
    beams[:] = new_beams
total_timelines = sum(num_timelines for is_beam, num_timelines in beams)
print(f"answer: {total_timelines}")
