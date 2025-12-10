#!/bin/python

with open("3.txt", "r") as input_file:
    banks = list(list(map(int, line.rstrip())) for line in input_file.readlines())
total = 0
for bank in banks:
    first_digit = 0
    first_digit_index = 0
    for i in range(len(bank) - 1):
        battery = bank[i]
        if battery > first_digit:
            first_digit = battery
            first_digit_index = i
    second_digit = max(battery for battery in bank[first_digit_index + 1:])
    total += first_digit * 10 + second_digit
print(f"answer: {total}")
