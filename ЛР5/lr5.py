import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
import numpy as np
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D


def f(x, y, z):
    return 2 * x ** 2 + y ** 2 - 2 * x - y + z + z ** 3

def F(params):
    
    x_val, y_val = params
    # Определение символов
    x, y, z = sp.symbols('x y z')

    # Неявное уравнение
    equation = 2 * x ** 2 + y ** 2 - 2 * x - y + z + z ** 3

    # Преобразование уравнения в функцию
    function = sp.lambdify((x, y, z), equation, 'numpy')

    # Численное решение
    solution = fsolve(lambda z: function(x_val, y_val, z)[0], 0)

    return solution[0]

initial_guess = [1, 1]

# Минимизация методом градиентного спуска
result= minimize(F, initial_guess, method='Nelder-Mead')
print('Result:', result.fun, result.x)

# Минимизация методом Нелдера-Мида
result= minimize(F, initial_guess, method='Powell')
print('Result:', result.fun, result.x)
