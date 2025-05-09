"""
Лабораторная работа №11. Расскраска графа.
https://publications.hse.ru/pubs/share/folder/0rhqzr8ukk/133671897.pdf
"""

def graph_colouring(V: list[int], E: list[set]) -> dict:
    A = build_adjacency_matrix(V, E)

    n = len(V)
    colours = [None] * n

    counter = 0
    while V:
        counter += 1
        i = V[0]
        colours[i] = counter
        V.remove(i)
        while 0 in A[i]:
            j = A[i].index(0)
            if j in V:
                colours[j] = counter
                V.remove(j)
                for _ in range(n):
                    if A[i][_] == 1 or A[j][_] == 1:
                        A[i][_] = 1
            else:
                A[i][j] = 1

    return colours, counter

def build_adjacency_matrix(V: list[int], E: list[set]) -> list[list[int]]:  # составлеение матрицы смежности
    n = len(V)
    A = [[0]*n for i in range(n)]
    for e in E:
        a, b = e[0], e[1]
        A[a][b] = 1
        A[b][a] = 1
    for i in range(n):
        A[i][i] = 1
    return A


V = [0, 1, 2, 3, 4, 5, 6]
E = [(0, 1), (0, 2), (0, 6), (1, 2), (1, 3), 
     (2, 3), (2, 5), (2, 6), (3, 4), (3, 6), (4, 5)]

colours, chromatic_number = graph_colouring(V, E)
print(f"Хроматическое число грава: {chromatic_number}, вершины имеют цвета {colours}")
