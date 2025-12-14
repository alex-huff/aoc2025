#!/bin/python

with open("6.txt", "r") as input_file:
    lines = input_file.readlines()
operators = []
i = 0
while i < len(lines[-1]):
    operator = lines[-1][i]
    operator_index = i
    i += 1
    while i < len(lines[-1]) and lines[-1][i] in " \n":
        i += 1
    operators.append((operator, (i - 1) - operator_index, operator_index))
total = sum(
    eval(
        operator.join(
            "".join(lines[j][i] for j in range(len(lines) - 1))
            for i in range(operator_index + width - 1, operator_index - 1, -1)
        )
    )
    for operator, width, operator_index in operators
)
print(f"answer: {total}")
