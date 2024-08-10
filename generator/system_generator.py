import random
import numpy as np

def generate_system_of_linear_equations():
    """Генерирует систему линейных уравнений с ограниченными коэффициентами и возвращает коэффициенты в виде матрицы и вектора."""
    a1 = random.randint(-5, 5)
    b1 = random.randint(-5, 5)
    c1 = random.randint(-10, 10)
    a2 = random.randint(-5, 5)
    b2 = random.randint(-5, 5)
    c2 = random.randint(-10, 10)
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    return A, B
