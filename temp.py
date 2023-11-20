import sympy as sp

# Определяем символы x и y
x, y = sp.symbols('x y')

x = 2
# Определяем уравнение
equation = x**2 + y ** 2 - 4

# Решаем уравнение относительно y
solution = sp.solve(equation, y)

print(solution)