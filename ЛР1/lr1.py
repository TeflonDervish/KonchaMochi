import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np
import sympy as sp


def f(x, y):
    return 3 * x**4 * y**5 + sp.exp(7 * x - 4 * y) - 4 * x**5 - 2 * y**4

def F(x_val):
    # Определение символов
    x, y = sp.symbols('x y')

    # Неявное уравнение
    equation = 3 * x**4 * y**5 + sp.exp(7 * x - 4 * y) - 4 * x**5 - 2 * y**4

    # Преобразование уравнения в функцию
    function = sp.lambdify((x, y), equation, 'numpy')

    # Начальное приближение для численного метода
    initial = [1, 1]

    # Численное решение
    solution = fsolve(lambda у: function(x_val, у)[0], 1)

    return x_val, solution[0]

# Пример использования функции
значение_x = 2
результат = F(значение_x)
print(f"x = {результат[0]}, y = {результат[1]}")




# Создание сетки точек
x_vals = np.linspace(-10, 10, 400)
y_vals = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Вычисление значений F(x, y)
Z = f(X, Y)

# Построение графика
plt.contour(X, Y, Z, levels=[0], colors='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График уравнения F(x, y) = 0')
plt.grid(True)
plt.show()
