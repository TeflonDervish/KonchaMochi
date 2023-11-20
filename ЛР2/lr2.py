from scipy import integrate
import numpy as np

# Заданная функция f(x, y)
def f(x, y):
    return np.sqrt(x**2 + y**2)

# Вычисление двойного интеграла первый метод
result, error = integrate.dblquad(f, -np.sqrt(4), np.sqrt(4), lambda x: -np.sqrt(4 - x**2), lambda x: np.sqrt(4 - x**2), epsabs=1e-6)

# Вывод результата
print("Double Integral First method:", result)
print("Error:", f"{error * 100}%")



# Пределы интегрирования
x_lower, x_upper = -np.sqrt(4), np.sqrt(4)
y_lower = lambda x: -np.sqrt(4 - x**2)
y_upper = lambda x: np.sqrt(4 - x**2)

# Вычисление двойного интеграла второй метод
result, error = integrate.quad(lambda x: integrate.quad(lambda y: f(x, y), y_lower(x), y_upper(x), epsabs=1e-7)[0], x_lower, x_upper, epsabs=1e-6)

# Вывод результата
print("Double Integral Second method:", result)
print("Error:", f"{error * 100}%")