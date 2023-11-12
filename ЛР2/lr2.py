from scipy import integrate
import numpy as np

# Заданная функция f(x, y)
def f(x, y):
    return np.sqrt(x**2 + y**2)

# Вычисление двойного интеграла
result, error = integrate.dblquad(f, -2, 2, lambda x: -np.sqrt(4 - x**2), lambda x: np.sqrt(4 - x**2))

# Вывод результата
print("Значение двойного интеграла:", result)
print("Ошибка:", error)



# Пределы интегрирования
x_lower, x_upper = -2, 2
y_lower = lambda x: -np.sqrt(4 - x**2)
y_upper = lambda x: np.sqrt(4 - x**2)

# Вычисление двойного интеграла
result, error = integrate.quad(lambda x: integrate.quad(lambda y: f(x, y), y_lower(x), y_upper(x))[0], x_lower, x_upper)

# Вывод результата
print("Значение двойного интеграла:", result)
print("Ошибка:", error)