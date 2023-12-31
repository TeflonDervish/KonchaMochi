from scipy.optimize import minimize
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Заданные наборы данных
x = np.array([2.51283,   3.11835,   3.60944,   4.02783,   4.39540,   4.72519,   5.02565,   5.30259,   5.56017,   5.80153])  # Пример значений x
y = np.array([2.60395,   2.58483,   2.69554,   2.84674,   3.00674,   3.16476,   3.31754,   3.46444,   3.60567,   3.74170])  # Пример значений y
z = np.array([[115.6189270,  112.2971039,  132.5746918,  164.6069183,  204.5376892,  250.7542419,  302.5302124,  359.5373230,  421.6294250,  488.7427063],
                [115.9274521,  112.6056290,  132.8832245,  164.9154510,  204.8462219,  251.0627594,  302.8387451,  359.8458557,  421.9379578,  489.0512390],
                [116.1776733,  112.8558578,  133.1334381,  165.1656647,  205.0964508,  251.3129883,  303.0889587,  360.0960693,  422.1881714,  489.3014526],
                [116.3908539,  113.0690384,  133.3466187,  165.3788452,  205.3096313,  251.5261688,  303.3021545,  360.3092651,  422.4013672,  489.5146484],
                [116.5781403,  113.2563248,  133.5339050,  165.5661316,  205.4969177,  251.7134552,  303.4894409,  360.4965515,  422.5886536,  489.7019348],
                [116.7461777,  113.4243622,  133.7019501,  165.7341766,  205.6649475,  251.8814850,  303.6574707,  360.6645813,  422.7566833,  489.8699646],
                [116.8992691,  113.5774536,  133.8550415,  165.8872681,  205.8180389,  252.0345764,  303.8105774,  360.8176575,  422.9097900,  490.0230713],
                [117.0403748,  113.7185593,  133.9961395,  166.0283661,  205.9591522,  252.1756897,  303.9516602,  360.9587708,  423.0508728,  490.1641541],
                [117.1716232,  113.8498077,  134.1273956,  166.1596222,  206.0903931,  252.3069305,  304.0829163,  361.0900269,  423.1821289,  490.2954102],
                [117.2946014,  113.9727859,  134.2503662,  166.2825928,  206.2133789,  252.4299164,  304.2059021,  361.2130127,  423.3051147,  490.4183960]])  # Пример значений z_ij



# Определение функции, которую будем минимизировать
def objective_function(params):
    a, b = params
    error_val = 0
    for i in range(len(x)):
        for j in range(len(y)):
            error_val += ((a * x[i] + b * y[j] ** 4) - z[i][j]) ** 2
    
    return error_val

# Начальные значения параметров a и b
initial_params = [1.0, 1.0]

# Минимизация функции для нахождения оптимальных параметров
result1 = minimize(objective_function, initial_params, method='BFGS')

result2 = minimize(objective_function, initial_params, method='Nelder-Mead')

# Получение оптимальных значений параметров a и b
optimal_params1 = result1.x
optimal_params2 = result2.x
# Вывод результата
print("Gradient descent")
print("Optimal values a and b:", optimal_params1)
print("Function minimum:", objective_function(optimal_params1))
print("\nMethod Nelder-Mead")
print("Optimal values a and b:", optimal_params2)
print("Function minimum:", objective_function(optimal_params2))



def func_for_plot(x, y):
    return optimal_params1[0]*x + optimal_params1[1]*(y**4)


a_values = np.linspace(2, 6, 100)
b_values = np.linspace(2, 5, 100)

# Вычисление значений функции для каждой комбинации a и b
A, B = np.meshgrid(a_values, b_values)
Z = np.zeros_like(A)
for i in range(len(a_values)):
    for j in range(len(b_values)):
        Z[i, j] = func_for_plot(A[i, j], B[i, j])

# Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, Z, cmap='viridis', alpha=0.5, label='Z')

x_mesh, y_mesh = np.meshgrid(x, y)
ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z.flatten(), color='red', label='Заданные точки')

ax.set_xlabel('Параметр a')
ax.set_ylabel('Параметр b')
ax.set_zlabel('Значение функции')
ax.set_title('Зависимость функции от параметров a и b')

plt.show()

x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Пример значений x
y1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Пример значений y
z1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],])  # Пример значений z_ij



def objective_function1(params):
        a, b = params
        error_val = 0
        for i in range(len(x1)):
            for j in range(len(y1)):
                error_val += ((a * x1[i] + b * y1[j] ** 4) - z1[i][j]) ** 2
        
        return error_val



initial_params = [1.0, 1.0]

    # Минимизация функции для нахождения оптимальных параметров
result1 = minimize(objective_function1, initial_params, method='BFGS')

result2 = minimize(objective_function1, initial_params, method='Nelder-Mead')

    # Получение оптимальных значений параметров a и b
optimal_params1 = result1.x
optimal_params2 = result2.x
    # Вывод результата
print("\nGradient descent")
print("Optimal values a and b:", optimal_params1)
print("\nMethod Nelder-Mead")
print("Optimal values a and b:", optimal_params2)


def func_for_plot1(x, y):
        return optimal_params1[0]*x + optimal_params1[1]*(y**4)


a_values = np.linspace(0, 10, 100)
b_values = np.linspace(0, 10, 100)

# Вычисление значений функции для каждой комбинации a и b
A, B = np.meshgrid(a_values, b_values)
Z = np.zeros_like(A)
for i in range(len(a_values)):
        for j in range(len(b_values)):
            Z[i, j] = func_for_plot1(A[i, j], B[i, j])

    # Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, Z, cmap='viridis', alpha=0.5, label='Z')

x_mesh, y_mesh = np.meshgrid(x1, y1)
ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z1.flatten(), color='red', label='Заданные точки')

ax.set_xlabel('Параметр a')
ax.set_ylabel('Параметр b')
ax.set_zlabel('Значение функции')
ax.set_title('Зависимость функции от параметров a и b')

plt.show()