import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np
import sympy as sp

def f(x, y):
    return 3 * x**4 * y**5 + sp.exp(7 * x - 4 * y) - 4 * x**5 - 2 * y**4


# Генерация значений x и y
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Создание сетки значений x и y
X, Y = np.meshgrid(x, y)

# Вычисление значений функции неявного уравнения
Z = f(X, Y)

# Построение графика контуров
plt.(X, Y, Z, levels=[0], colors='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour Plot of the Implicit Equation')
plt.grid(True)
plt.show()