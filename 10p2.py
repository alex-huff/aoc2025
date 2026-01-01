#!/bin/python

import itertools
import math


def parse_machine_description(desc_str):
    i = 1
    desc = []

    def skip_space():
        nonlocal i
        while desc_str[i] == " ":
            i += 1

    def parse_till(target_char):
        nonlocal i
        starting_index = i
        while desc_str[i] != target_char:
            i += 1
        return desc_str[starting_index:i]

    light_diagram_str = parse_till("]")
    light_diagram = [c == "#" for c in light_diagram_str]
    i += 1
    skip_space()
    desc.append(light_diagram)
    button_wiring_schematics = []
    while desc_str[i] == "(":
        i += 1
        button_wiring_schematic_str = parse_till(")")
        button_wiring_schematics.append(
            list(map(int, button_wiring_schematic_str.split(",")))
        )
        i += 1
        skip_space()
    desc.append(button_wiring_schematics)
    i += 1
    joltage_requirements_str = parse_till("}")
    joltage_requirements = list(map(int, joltage_requirements_str.split(",")))
    desc.append(joltage_requirements)
    return desc


def precalculate_button_properties(button_wiring_schematics, target_joltage_levels):
    properties = []
    for i, current_button in enumerate(button_wiring_schematics):
        last_provider_of = [
            wire in current_button for wire in range(len(target_joltage_levels))
        ]
        guarrenteed_collateral = [None for _ in range(len(target_joltage_levels))]
        for j in range(i + 1, len(button_wiring_schematics), 1):
            other_button = button_wiring_schematics[j]
            for wire in other_button:
                last_provider_of[wire] = False
                collateral = {
                    other_wire for other_wire in other_button if other_wire != wire
                }
                if guarrenteed_collateral[wire] is None:
                    guarrenteed_collateral[wire] = collateral
                else:
                    guarrenteed_collateral[wire] &= collateral
        guarrenteed_collateral = [
            set() if collateral is None else collateral
            for collateral in guarrenteed_collateral
        ]
        properties.append((last_provider_of, guarrenteed_collateral))
    return properties


def lowest_presses_to_target_configuration(
    target_joltage_levels,
    button_wiring_schematics,
    i,
    current_joltage_levels,
    current_presses,
    button_properties,
    lowest_presses_found,
):
    if i == len(button_wiring_schematics):
        return current_presses
    current_button = button_wiring_schematics[i]
    last_provider_of, guarrenteed_collateral = button_properties[i]
    max_possible_presses_without_overlow = min(
        target_joltage_levels[wire] - current_joltage_levels[wire]
        for wire in current_button
    )
    last_chance_presses_to_satisfy_joltage_requirements = {
        target_joltage_levels[wire] - current_joltage_levels[wire]
        for wire, is_last_provider in enumerate(last_provider_of)
        if is_last_provider
    }
    if len(last_chance_presses_to_satisfy_joltage_requirements) > 1:
        return math.inf
    elif len(last_chance_presses_to_satisfy_joltage_requirements) == 1:
        presses = next(iter(last_chance_presses_to_satisfy_joltage_requirements))
        if presses > max_possible_presses_without_overlow:
            return math.inf
        lower_bound = upper_bound = presses
    else:
        lower_bound, upper_bound = (0, max_possible_presses_without_overlow)
    for wire in current_button:
        collateral = guarrenteed_collateral[wire]
        if not collateral:
            continue
        max_joltage_provided_by_later_buttons_till_overflow = min(
            (target_joltage_levels[other_wire] - current_joltage_levels[other_wire])
            for other_wire in collateral
        )
        # this can be lower since there are inter-dependencies that I didn't consider
        lower_bound = max(
            (target_joltage_levels[wire] - current_joltage_levels[wire])
            - max_joltage_provided_by_later_buttons_till_overflow,
            lower_bound,
        )
        # also upper bound can be lowered too!
        # BUT IT WORKS GOOD ENOUGH
        # I feel like I am missing something this seems very complicated
        if lower_bound > upper_bound:
            return math.inf
    min_presses = math.inf
    for j in range(upper_bound, lower_bound - 1, -1):
        if current_presses + j >= lowest_presses_found[0]:
            break
        for wire in current_button:
            current_joltage_levels[wire] += j
        min_total_presses_for_j_presses_of_button = (
            lowest_presses_to_target_configuration(
                target_joltage_levels,
                button_wiring_schematics,
                i + 1,
                current_joltage_levels,
                current_presses + j,
                button_properties,
                lowest_presses_found,
            )
        )
        for wire in current_button:
            current_joltage_levels[wire] -= j
        if min_total_presses_for_j_presses_of_button < min_presses:
            min_presses = min_total_presses_for_j_presses_of_button
            if min_presses < lowest_presses_found[0]:
                lowest_presses_found[0] = min_presses
    return min_presses


with open("10.txt", "r") as input_file:
    machines = list(
        map(
            lambda line: parse_machine_description(line.rstrip()),
            input_file.readlines(),
        )
    )
total_presses = 0
for machine in machines:
    light_diagram, button_wiring_schematics, joltage_requirements = machine
    button_wiring_schematics = sorted(
        button_wiring_schematics, key=lambda schem: len(schem), reverse=True
    )
    button_properties = precalculate_button_properties(
        button_wiring_schematics, joltage_requirements
    )
    total_presses += lowest_presses_to_target_configuration(
        joltage_requirements,
        button_wiring_schematics,
        0,
        [0 for _ in range(len(joltage_requirements))],
        0,
        button_properties,
        [math.inf],
    )
print(f"answer: {total_presses}")
