#!/bin/python

import itertools


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


def lowest_presses_to_target_configuration(
    target_light_configuration, button_wiring_schematics
):
    def do_button_press(lights, button_wiring_schematic):
        for wire in button_wiring_schematic:
            lights[wire] = not lights[wire]

    for i in range(1, len(button_wiring_schematics) + 1, 1):
        for button_subset in itertools.combinations(button_wiring_schematics, i):
            lights = [False for _ in range(len(light_diagram))]
            for button_wiring_schematic in button_subset:
                do_button_press(lights, button_wiring_schematic)
            if lights == target_light_configuration:
                return i


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
    total_presses += lowest_presses_to_target_configuration(
        light_diagram, button_wiring_schematics
    )
print(f"answer: {total_presses}")
