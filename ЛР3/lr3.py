from sympy import symbols, cos, integrate
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


# Определение функции f(x, alpha)
def f(x, alpha):
    return np.cos(alpha * x ** 2)

# Определение пределов интегрирования
a = 1
b = 2

# Определение функции, которую будем минимизировать (интеграл от f по x на интервале [a, b])
def objective_function(alpha):
    result, _ = quad(lambda x: f(x, alpha), a, b)
    return result

# Начальное значение параметра alpha
initial_alpha = 1.0

# Минимизация функции с помощью градиентного спуска
result = minimize(objective_function, initial_alpha, method='BFGS')

# Получение оптимального значения параметра alpha
optimal_alpha = result.x[0]

# Вывод результата
print("Optimal alpha with gradient spusk:", optimal_alpha)
print("minimum:", result.fun)

# Минимизация функции с помощью метода Нелдера-Мида
result = minimize(objective_function, initial_alpha, method='Nelder-Mead')

# Получение оптимального значения параметра alpha
optimal_alpha = result.x[0]

# Вывод результата
print("Optimal alpha with Nelder-Mead alpha:", optimal_alpha)
print("minimum:", result.fun)



# График зависимости интеграла от значения alpha
alphas = np.linspace(-10, 10, 1000)
integral_values = [quad(lambda x: f(x, alpha), a, b)[0] for alpha in alphas]

plt.plot(alphas, integral_values, label=r'$\int_{1}^{2} \cos(\alpha x^2) \, dx$')
plt.title('Зависимость интеграла от параметра alpha')
plt.xlabel(r'$\alpha$')
plt.ylabel('Значение интеграла')
plt.legend()
plt.grid(True)
plt.show()

