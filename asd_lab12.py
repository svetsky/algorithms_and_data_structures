# Лабораторная работа №12. Задача о ранце.
# Задача: имеется ранец вместимостью c, n товаров, известна стоимость и вес каждого товара. 
# Необходмо выбрать товары, чтьобы из стоимость была максимальной, а суммарный вес не превышал вместимость ранца.

def knapsack(values: list[int], weights: list[int], c: int) -> int:
    n = len(values)

    A = [[0] * (c + 1) for i in range(n + 1)]     

    for i in range(1, n+1):
        for j in range(1, c+1):
            if weights[i-1] > j:
                A[i][j] = A[i - 1][j]
            else:
                A[i][j] = max(A[i - 1][j],A[i - 1][j - weights[i - 1]] + values[i - 1])

    return A[n][c], A

def knapsack_reconstruction(A: list[list[int]], values: list[int], weights: list[int], c: int) -> list[int]:
    n = len(values)
    S = []

    for i in range(n, 0, -1):
        if weights[i - 1] <= c and A[i - 1][c - weights[i - 1]] + values[i - 1] >= A[i - 1][c]:
            S.append(i - 1)
            c = c - weights[i - 1]
        else: continue
    return sorted(S)

values  = [3, 2, 4, 4]      # стоимость товаров
weights = [4, 3, 2, 3]      # вес товаров   
capacity = 6                # вместимость ранца

max_value, A = knapsack(values, weights, capacity)
goods = knapsack_reconstruction(A, values, weights, capacity)
print(f"В ранце товары под индексами {goods} общей стоимостью {max_value}.")
