import numpy as np

def solve_system_of_linear_equations(A, B):
    """Решает систему линейных уравнений вида Ax = B и возвращает округленные до двух знаков корни x и y в виде строки, разделённой запятыми."""
    try:
        solution = np.linalg.solve(A, B)
        return f"{round(solution[0], 2)},{round(solution[1], 2)}"
    except np.linalg.LinAlgError:
        return None
