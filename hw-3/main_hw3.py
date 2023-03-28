import numpy as np

# 1
arr = np.zeros(10)
arr [4] = 1

arr_2d = arr.reshape((2, 5))

# 2 

arr = np.arange(10, 50)
arr = np.flip(arr)
evens = arr[arr % 2 == 0]

# 3

arr = np.arange(9).reshape(3,3)
print(arr)

# 4

arr = random.rand(4, 3, 2)

arr_min = np.min(arr)
arr_max = np.max(arr)

# 5 

arr1 = np.random.rand(6, 4)
arr2 = np.random.rand(4, 3)

result = np.dot(arr1, arr2)
print("Первый массив:\n", arr1)
print("Второй массив:\n", arr1)
print("Результат матричного умножения:\n", result)

# 6 

arr = np.random.rand(7, 7)

arr_mean = np.mean(arr)
arr_std = np.std(arr)

arr_normilized = (arr - arr_mean) / arr_std

print("Случайный массив:\n", arr)
print("Среднее:\n", arr_mean)
print("Стандартное отклонение:\n", arr_std)
print("Нормализованный массив:\n", arr_normilized)

# Pandas && Visualization
import pandas as pd
import mathplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())
print("Количество строк и колонок:", tips.shape)
print("Пропущенные Значения:\n", tips.isna().sum())

numerical_cols = ['total_bill', 'tip', 'size']
sns.histplot(data = tips[numerical_cols])
plt.show()

print("Максимальное значениеtotal_bill:", tips['total_bill'].max())
print("Количество курящих людей:", tips['smoker'].value_counts()[1])

mean_total_bill_by_day = tips.groupby('day')[total_bill].mean()
print("Среднй total_bill в зависимости от дня недели:\n", mean_total_bill_by_day)

meadian_total_bill = tips['total_bill'].median()
high_total_bill_tips = tips[tips['total_bill'] > median_total_bill]
mean_tip_by_sex = hightotal_billtips.groupby('sex')['tip'].mean()
print("Средний tip для людейс  total_bill > медианы в зависимости от пола:\n", mean_tip_by_sex)

tips['smoker'] = tips['smoker'].map({'Yes': 1, 'No': 0})

sns.histplot(data=tips, x='total_bill', y='tip')
plt.show()
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

sns.pairplot(data=tips)
plt.show()

sns.catplot(data=tips, x='tip', y='total_bill')
plt.show()

sns.histplot(data=tips, x='tip', hue='time', multiple='stack')
plt.show()

sns.scatterplot(data=tips[tips['sex'] == 'Male'], x='total_bill', y='tip', hue='smoker')
plt.show()

sns.scatterplot(data=tips[tips['sex'] == 'Female'], x='total_bill', y='tip', hue='smoker')
plt.show()



