#!/bin/python

import math

with open("2.txt", "r") as input_file:
    ranges = [
        tuple(map(int, range.split("-"))) for range in input_file.read().split(",")
    ]


def num_digits(number):
    if not number:
        return 1
    return math.floor(math.log10(abs(number))) + 1


def digits_doubled(number):
    return number * (10 ** num_digits(number)) + number


sum_of_invalid_ids = 0
for id_range in ranges:
    lower, upper = id_range
    num_digits_lower = num_digits(lower)
    num_digits_upper = num_digits(upper)
    if num_digits_lower % 2 == 1:
        lower = 10**num_digits_lower + 10 ** ((num_digits_lower + 1) // 2 - 1)
        num_digits_lower += 1
    if num_digits_upper % 2 == 1:
        upper = 10 ** (num_digits_upper - 1) - 1
        num_digits_upper -= 1
    if lower > upper:
        continue
    lower_half = int(str(lower)[: num_digits_lower // 2])
    upper_half = int(str(upper)[: num_digits_upper // 2])
    if lower_half > upper_half:
        continue
    sum_of_invalid_ids += sum(
        filter(
            lambda id: lower <= id <= upper,
            (digits_doubled(half) for half in range(lower_half, upper_half + 1)),
        )
    )
print(f"answer: {sum_of_invalid_ids}")
