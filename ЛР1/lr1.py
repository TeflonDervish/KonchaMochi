import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
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

    # Численное решение
    solution = fsolve(lambda у: function(x_val, у)[0], 0)

    return solution[0]

# Минимизация методом градиентного спуска
result= minimize(F, 0, method='BFGS')
print("Gradient Descent")
print(f"F(xmin,ymin) = {f(result.x[0], result.fun)}")
print("y'(xmin)=: ", result.fun)
print("X value: ", result.x[0])

# Минимизация методом Нелдера-Мида
result= minimize(F, 0, method='Nelder-Mead')
print("\nNelder-Mead")
print(f"F(xmin,ymin) = {f(result.x[0], result.fun)}")
print("y'(xmin)=: ", result.fun)
print("X value: ", result.x[0])


# Иницализация значений для графика
x_values = np.linspace(-0.5, 0.5, 100)
y_values = []

# Значение Y для функции
for x_val in x_values:
    result = F(x_val)
    y_values.append(result)

# Отрисовка графика
plt.plot(x_values, y_values, label='Implicit Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the Implicit Equation')
plt.legend()
plt.grid(True)
plt.show()
