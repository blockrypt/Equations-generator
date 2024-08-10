import numpy as np

def solve_linear_equation(a, b):
    """Решение линейного уравнения вида ax + b = 0"""
    return -b / a

def solve_quadratic_equation(a, b, c):
    """Решение квадратного уравнения вида ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + np.sqrt(discriminant)) / (2 * a)
        x2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return f"{round(x1, 2)}, {round(x2, 2)}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"{round(x, 2)}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(-discriminant) / (2 * a)
        x1 = f"{round(real_part, 2)}+{round(imaginary_part, 2)}i"
        x2 = f"{round(real_part, 2)}-{round(imaginary_part, 2)}i"
        return f"{x1}, {x2}"

def solve_system_of_linear_equations(A, B):
    """Решение системы линейных уравнений вида Ax = B"""
    try:
        solution = np.linalg.solve(A, B)
        return f"{round(solution[0], 2)}, {round(solution[1], 2)}"
    except np.linalg.LinAlgError:
        return None
