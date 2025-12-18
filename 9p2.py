#!/bin/python


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def is_vertical_edge(edge):
    return edge[0][0] == edge[1][0]


def in_range(num, a, b):
    min_bound = min(a, b)
    max_bound = max(a, b)
    return min_bound < num < max_bound


def perpendicular_lines_intersect(a, b):
    a_is_vertical = is_vertical_edge(a)
    vertical_line = a if a_is_vertical else b
    horizontal_line = b if a_is_vertical else a
    return in_range(
        vertical_line[0][0], horizontal_line[0][0], horizontal_line[1][0]
    ) and in_range(horizontal_line[0][1], vertical_line[0][1], vertical_line[1][1])


def is_in_line(line, pos):
    line_is_vertical = is_vertical_edge(line)
    if line_is_vertical:
        return pos[0] == line[0][0] and in_range(pos[1], line[0][1], line[1][1])
    return pos[1] == line[0][1] and in_range(pos[0], line[0][0], line[1][0])


def is_in_loop(pos):
    return (
        len(
            [
                edge
                for edge in edges
                if (
                    is_vertical_edge(edge)
                    and edge[0][0] > pos[0]
                    and in_range(pos[1], edge[0][1], edge[1][1])
                )
            ]
        )
        % 2
        == 1
    )


def is_concave(vertex_index):
    prev_vertex = vertices[vertex_index - 1]
    vertex = vertices[vertex_index]
    next_vertex = vertices[(vertex_index + 1) % len(vertices)]
    diff_prev = (vertex[0] - prev_vertex[0], vertex[1] - prev_vertex[1])
    diff_next = (vertex[0] - next_vertex[0], vertex[1] - next_vertex[1])
    diff_adjacent = (diff_prev[0] + diff_next[0], diff_prev[1] + diff_next[1])
    diff_adjacent_bump = (
        (diff_adjacent[0] / abs(diff_adjacent[0])) * 0.1,
        (diff_adjacent[1] / abs(diff_adjacent[1])) * 0.1,
    )
    return is_in_loop(
        (vertex[0] + diff_adjacent_bump[0], vertex[1] + diff_adjacent_bump[1])
    )


def line_segments_dont_overlap(a, b):
    dimension = int(is_vertical_edge(a))
    a_min = min(a[0][dimension], a[1][dimension])
    a_max = max(a[0][dimension], a[1][dimension])
    b_min = min(b[0][dimension], b[1][dimension])
    b_max = max(b[0][dimension], b[1][dimension])
    return b_min >= a_max or a_min >= b_max


def line_extends_off_of_convex_vertex(line):
    line_is_vertical = is_vertical_edge(line)
    touching_convex_verticies = [
        (vertices_dict[edge], edge)
        for edge in line
        if edge in vertices_dict and not concavity[vertices_dict[edge]]
    ]
    for vertex_index, vertex in touching_convex_verticies:
        adjacent_edges = (edges[vertex_index], edges[(vertex_index + 1) % len(edges)])
        parellel_adjacent_edge = next(
            filter(
                lambda edge: is_vertical_edge(edge) == line_is_vertical, adjacent_edges
            )
        )
        if line_segments_dont_overlap(parellel_adjacent_edge, line):
            return True
    return False


def line_crosses_loop(line):
    line_is_vertical = is_vertical_edge(line)
    perpendicular_edges = filter(
        lambda edge: is_vertical_edge(edge) != line_is_vertical, edges
    )
    intersecting_perpendicular_edges = filter(
        lambda edge: perpendicular_lines_intersect(edge, line),
        perpendicular_edges,
    )
    if any(True for edge in intersecting_perpendicular_edges):
        return True
    if any(
        (not concavity[vertex_index] and is_in_line(line, vertex))
        for vertex_index, vertex in enumerate(vertices)
    ):
        return True
    return line_extends_off_of_convex_vertex(line)


def rectangle_in_loop(a, b):
    rectangle_edges = (
        ((a[0], a[1]), (b[0], a[1])),
        ((a[0], a[1]), (a[0], b[1])),
        ((b[0], b[1]), (a[0], b[1])),
        ((b[0], b[1]), (b[0], a[1])),
    )
    return not any(line_crosses_loop(edge) for edge in rectangle_edges)


with open("9.txt", "r") as input_file:
    vertices = [
        tuple(map(int, line.split(",")))
        for line in map(str.rstrip, input_file.readlines())
    ]
vertices_dict = {vertex: i for i, vertex in enumerate(vertices)}
edges = [(vertices[i], vertices[i + 1]) for i in range(-1, len(vertices) - 1, 1)]
concavity = [is_concave(i) for i in range(len(vertices))]
largest_area = 0
for i in range(len(vertices) - 1):
    for j in range(i + 1, len(vertices) - 1):
        a, b = vertices[i], vertices[j]
        rectangle_area = area(a, b)
        if rectangle_area < largest_area or not rectangle_in_loop(a, b):
            continue
        largest_area = rectangle_area
print(f"answer: {largest_area}")
