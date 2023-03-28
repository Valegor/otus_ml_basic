# 1 task

import numpy as np

def share_bread(N, K):
    x = K // N
    y = K % N
    return  x, y

assert share_bread(N=3, K=14) == (4, 2)


# 2 задание

def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return  'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'
# 3

def amulet_area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

# 4

def cal_euclidean(a, b):
    return np.sqrt(np.sum(np.square(a - b)))

def cal_manhattan(a, b):
    return np.sum(np.abs(a - b))

def cal_cosine(a, b):
    return 1 - np.dot(a, b) / (np.sqrt(np.sum(np.square(a))) * np.sqrt(np.sum(np.square(b))))

# 5
# создание случайного массива
arr = np.random.rand(100)

# нахождение max и min 
max_val = np.max(arr)
min_val == np.min(arr)

# Преобразование массива
arr = (arr - min_val) / (max_val - min_val)
arr[arr == np.max(arr)] = 1
print(np.max(arr), np.min(arr))
print(arr)

########

matrix = np.random.randit(0, 50, (5, 6))
# находим максимальное значение в матрице
max_value = np.max(matrix) 

# находим индексы максимального значения в матрице
max_index = np.where(matrix == max_value)[1][0]

print(f"Колонка с максимальным элементом: {matrix[:, max_index]}")

#####

def get_unique_rows(X):
    unique_rows = np.unique(X, axis=0)
    return unique_rows

X = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7 ,8, 9]])
unique_rows = get_unique_rows(X)
print(unique_rows)