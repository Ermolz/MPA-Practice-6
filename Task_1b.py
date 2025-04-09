def can_color_with_k_colors_improved(graph, k):
    n = len(graph)

    order = sorted(range(n), key=lambda v: len(graph[v]), reverse=True)

    color = [0] * n
    if backtrack_coloring_improved(graph, k, color, order, 0):
        return color
    else:
        return None


def backtrack_coloring_improved(graph, k, color, order, index):
    if index == len(order):
        return True

    vertex = order[index]

    for c in range(1, k + 1):
        if is_safe_to_color(graph, color, vertex, c):
            color[vertex] = c
            if backtrack_coloring_improved(graph, k, color, order, index + 1):
                return True
            color[vertex] = 0
    return False


def is_safe_to_color(graph, color, vertex, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True


def find_chromatic_number_improved(graph):
    n = len(graph)
    for k in range(1, n + 1):
        coloring = can_color_with_k_colors_improved(graph, k)
        if coloring is not None:
            return k, coloring
    return None


if __name__ == "__main__":
    #    0 -- 1
    #     \   /
    #      \ /
    #       2
    #       |
    #       3
    #       |
    #       4
    graph = [
        [1, 2],
        [0, 2],
        [0, 1, 3],
        [2, 4],
        [3]
    ]

    k = 5

    coloring_result = can_color_with_k_colors_improved(graph, k)

    if coloring_result is not None:
        print(f"Граф можна розфарбувати за допомогою {k} кольорів (покращена стратегія).")
        print("Отримане розфарбування (vertex: color):")
        for v, col in enumerate(coloring_result):
            print(f"  Вершина {v} -> колір {col}")
    else:
        print(f"Неможливо розфарбувати граф з {k} кольорами (покращена стратегія).")
