#!/bin/python

import math

with open("2.txt", "r") as input_file:
    ranges = [
        tuple(map(int, range.split("-"))) for range in input_file.read().split(",")
    ]


def digits_repeated(number, num_repeats):
    number_digits = num_digits(number)
    result = 0
    for i in range(num_repeats):
        result += number * (10 ** (number_digits * i))
    return result


def num_digits(number):
    if not number:
        return 1
    return math.floor(math.log10(abs(number))) + 1


# SO MANY MORE OPTIMIZATIONS POSSIBLE
invalid_ids = set()
for id_range in ranges:
    lower, upper = id_range
    num_digits_lower = num_digits(lower)
    num_digits_upper = num_digits(upper)
    for repeat_length in range(1, num_digits_upper // 2 + 1):
        lowest_repeat = 10 ** (repeat_length - 1)
        highest_repeat = 10**repeat_length - 1
        for repeat in range(lowest_repeat, highest_repeat + 1):
            min_repeats = num_digits_lower // repeat_length
            if num_digits_lower % repeat_length != 0:
                min_repeats += 1
            min_repeats = max(2, min_repeats)
            max_repeats = num_digits_upper // repeat_length
            for num_repeats in range(min_repeats, max_repeats + 1):
                id = digits_repeated(repeat, num_repeats)
                if lower <= id <= upper:
                    invalid_ids.add(id)
print(f"answer: {sum(invalid_ids)}")
