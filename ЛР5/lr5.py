import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
import numpy as np
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D

# 2 * x ** 2 + y ** 2 - 2 * x - y + z + z ** 3
# ((x + 2 * y - 1) / sp.sqrt(x * x + y * y + 1)) - z - 2.71828182845904 ** z

# 1 вар: x**4 - 2 * x ** 2 + 4 * x * y - 2 * y ** 2 + 3 - z - np.exp(z)
# 2 вар: sp.exp(x + y)*(2 * y ** 2 - x ** 2) - z - sp.exp(z)
# 3 вар: ((x + y - 1) / (sp.sqrt(x ** 2 + y ** 2 + 1))) - z - sp.exp(z)
# 4 вар: ((x + 2 * y - 1) / sp.sqrt(x * x + y * y + 1)) - z - 2.71828182845904 ** z
# 5 вар: sp.exp(x + y) * (2 * y ** 2 - x ** 2) - z - sp.atan(z)
# 6 вар: 3 * x **3 + y ** 2 + 4 * x * y - x - z - sp.exp(z)
# 7 вар: 3 * x **3 + y ** 2 + 4 * x * y - x - z - sp.atan(z)
# 8 вар: x ** 4 + x * y + y ** 2 - z - z ** 3
# 9 вар: 2 * x ** 2 + y ** 2 - 2 * x - y + z + z ** 3
# 10 вар: 2 * x ** 2 + y ** 2 - 2 * x - y + z + z ** 5
# 11 вар: x * y * sp.ln(x ** 2 + y ** 2) - z - z ** 3
# 12 вар: (x - 1) ** 2 + (y - 2) ** 2 - z - sp.exp(z)
# 13 вар: x * y * sp.ln(x ** 2 + y ** 2) - z - z ** 3
# 14 вар: x * y * sp.ln(2 * x ** 2 + y ** 2) - z - sp.exp(z)
# 15 вар: 
# 16 вар: 
# 17 вар: x ** 3 + 3 * x * y ** 2 - 15 * x - 12 * y - z - sp.exp(x)
# 18 вар: 
# 20 вар: 
# 21 вар: 
# 22 вар: 
# 23 вар: 
# 24 вар: 
# 25 вар: 
# 26 вар: 
# 27 вар: 
# 28 вар: 
# 29 вар: 
# 30 вар: 


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
result= minimize(F, initial_guess, method='Nelder-Mead', tol=1e-4)
print(result.x, result.fun)
print('Semenov BPO-21-01\nNelder-Mead')
print('xmin =', result.x[0], 'ymin =', result.x[1], 'zmin =', result.fun)
print('F(xmin, ymin, zmin) =', f(result.x[0], result.x[1], result.fun))

# Минимизация методом Нелдера-Мида
result= minimize(F, initial_guess, method='Powell', tol=1e-4)
print('Semenov BPO-21-01\nPowell')
print('xmin =', result.x[0], 'ymin =', result.x[1], 'zmin =', result.fun)
print('F(xmin, ymin, zmin) =', f(result.x[0], result.x[1], result.fun))


# -3.23630011678233e-14
# -1.54321000422897e-14