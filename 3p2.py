#!/bin/python

with open("3.txt", "r") as input_file:
    banks = list(list(map(int, line.rstrip())) for line in input_file.readlines())
total = 0
num_digits = 12
for bank in banks:
    digits = []
    last_digit_index = -1
    for i in range(num_digits):
        digits_left = num_digits - i
        highest_battery = 0
        highest_battery_index = last_digit_index + 1
        for j in range(last_digit_index + 1, len(bank) - (digits_left - 1)):
            battery = bank[j]
            if battery > highest_battery:
                highest_battery = battery
                highest_battery_index = j
        digits.append(highest_battery)
        last_digit_index = highest_battery_index
    battery_sum = sum(digit * 10**i for i, digit in enumerate(reversed(digits)))
    total += battery_sum
print(f"answer: {total}")
