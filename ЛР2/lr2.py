from scipy import integrate
import numpy as np

# Заданная функция f(x, y)
def f(x, y):
    return np.sqrt(x**2 + y**2)

# Область интегрирования S (круг с радиусом 2, так как 2^2 = 4)
def S(x, y):
    return x**2 + y**2 <= 4

# Вычисление двойного интеграла
result, error = integrate.nquad(f, [[-2, 2], [-2, 2]], S)

# Вывод результата
print("Значение двойного интеграла:", result)
print("Ошибка:", error)