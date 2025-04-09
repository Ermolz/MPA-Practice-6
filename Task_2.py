def greedy_coloring_largest_first(adj_list):
    n = len(adj_list)

    degrees = [len(adj_list[v]) for v in range(n)]

    sorted_vertices = sorted(range(n), key=lambda v: (-degrees[v], v))

    colorings = [0] * n

    for v in sorted_vertices:
        used_colors = set()

        for neighbor in adj_list[v]:
            if colorings[neighbor] != 0:
                used_colors.add(colorings[neighbor])

        color = 1
        while color in used_colors:
            color += 1

        colorings[v] = color

    return colorings


if __name__ == "__main__":
    #     0 -- 1
    #      \   /
    #       \ /
    #        2
    #        |
    #        3
    #        |
    #        4
    graph = [
        [1, 2],
        [0, 2],
        [0, 1, 3],
        [2, 4],
        [3]
    ]

    coloring_result = greedy_coloring_largest_first(graph)

    print("Жадібне розфарбування графа:")
    for v, color in enumerate(coloring_result):
        print(f"  Вершина {v} -> колір {color}")
