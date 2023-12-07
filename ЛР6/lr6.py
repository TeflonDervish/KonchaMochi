import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
import numpy as np
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D


x_data = np.array([6.1766,
                8.1305,
                9.7320,
                11.1603,
                12.4754,
                13.7070,
                14.8729,
                15.9852,
                17.0522,
                18.0802])
y_data = np.array([2.18610,
                1.96222,
                1.84003,
                1.75742,
                1.69609,
                1.64800,
                1.60887,
                1.57617,
                1.54829,
                1.52414])


def func(params, x):
    a, b, c =params
    return (a *  x ** 2 + b * x + c * x ** 3) ** (1 / x)

def objective(params):
    predictions = func(params, x_data)
    return np.sum((predictions - y_data) ** 2)

initial_params = [1, 1, 1]
result = minimize(objective, initial_params, method='nelder-mead')


print('Semenov Vyacheslav BPO-21-01\nMethod nelder-mead\na, b, c =', result.x)

result = minimize(objective, initial_params, method='BFGS')

print('Semenov Vyacheslav BPO-21-01\nMethod BFGS\na, b, c =', result.x)

x_val = np.linspace(1, 20, 100)
y_val = func(result.x, x_val)

plt.plot(x_val, y_val)
plt.scatter(x_data, y_data)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
