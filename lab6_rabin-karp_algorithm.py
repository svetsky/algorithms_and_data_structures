# Лабораторная работа №6. Алгоритм Рабина-Карпа.
# https://rutube.ru/video/9b6b215ecffce613e76aeaf96c8c9f0b/

def count_hash(T, x, k):
    h = 0
    for i in range(len(T)):
        h = (h * x + ord(T[i]) - 97) % k        # hash(P + c) = (hash(P) * x + c) mod k
    return h


def build_hash(T, P, x, k):         # полиномиальное хеширование
    n = len(T)
    m = len(P)
    hash_list = []
    for i in range(n - m + 1):
        if i == 0:
            hash_list.append(count_hash(T[:m], x, k))
        if i > 0:
            # пересчет хеш-функции при сдвиге на 1:
            hash_list.append((hash_list[i - 1] * x - (ord(T[i - 1]) - 97) * x ** m + (ord(T[i + m - 1]) - 97)) % k)
    return hash_list


def rabin_karp_algorithm(T, P):             # Алгоритм Рабина-Карпа
    x = 7
    k = 11
    n = len(T)
    m = len(P)
    p_hash = count_hash(P, x, k)            # хеш паттерна
    hash_list = build_hash(T, P, x, k)      # хеш каждой подстроки длины паттерна
    for i in range(n - m + 1):
        if hash_list[i] != p_hash:
            continue
        else:                               # если у паттерна и подстроки хеши совпадают, сравниваем их по символам
            flag = True
            for j in range(m):
                if T[i+j] != P[j]:
                    flag = False
                    break
            if flag:
                print("Образец обнаружен при сдвиге", i)


text = input('Введите текст ').lower()
pattern = input('Введите образец ').lower()
rabin_karp_algorithm(text, pattern)
