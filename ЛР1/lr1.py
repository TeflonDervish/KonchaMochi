from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# Заданная функция f(x, y)
def f(params):
    x, y = params
    return 3 * x ** 4 * y ** 5 + np.exp(7*x - 4*y) - 4 * x ** 5 - 2 * y ** 4

# Ограничение уравнением F(x, y) = 0 (пример: окружность радиуса 1)
def constraint(params):
    x, y = params
    return x**2 + y**2 - 1

# Начальные значения параметров x и y
initial_params = [0.0, 0.0]

# Определение ограничений
constraints = ({'type': 'eq', 'fun': constraint})

# Используем метод оптимизации для поиска минимума
result = minimize(f, initial_params, constraints=constraints, method='SLSQP')

# Получение оптимальных значений x и y
optimal_params = result.x

# Вывод результата
print("Оптимальные значения x и y:", optimal_params)
print("Минимум функции:", result.fun)

# Визуализация функции и уравнения F(x, y) = 0
x_vals = np.linspace(-2, 2, 100)
y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z_f = f([X, Y])
Z_F = constraint([X, Y])

# Построение графиков
plt.contour(X, Y, Z_F, levels=[0], colors='r', label='F(x, y) = 0')
plt.plot(optimal_params[0], optimal_params[1], 'bo', label='Минимум')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Функция f(x, y) и условие F(x, y) = 0')
plt.legend()
plt.show()