import random
import numpy as np

def generate_linear_equation(difficulty):
    """Генерация линейного уравнения в зависимости от уровня сложности"""
    if difficulty == 'easy':
        a = random.randint(1, 5)
        b = random.randint(-5, 5)
    elif difficulty == 'medium':
        a = random.randint(-10, 10)
        b = random.randint(-20, 20)
    elif difficulty == 'hard':
        a = random.randint(-20, 20)
        b = random.randint(-50, 50)
    while a == 0:
        a = random.randint(-20, 20)
    return a, b

def generate_quadratic_equation(difficulty):
    """Генерация квадратного уравнения в зависимости от уровня сложности"""
    if difficulty == 'easy':
        a = random.randint(1, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
    elif difficulty == 'medium':
        a = random.randint(-10, 10)
        b = random.randint(-20, 20)
        c = random.randint(-20, 20)
    elif difficulty == 'hard':
        a = random.randint(-20, 20)
        b = random.randint(-50, 50)
        c = random.randint(-50, 50)
    while a == 0:
        a = random.randint(-20, 20)
    return a, b, c

def generate_system_of_linear_equations(difficulty):
    """Генерация системы линейных уравнений в зависимости от уровня сложности"""
    if difficulty == 'easy':
        a1 = random.randint(1, 5)
        b1 = random.randint(-5, 5)
        c1 = random.randint(-5, 5)
        a2 = random.randint(1, 5)
        b2 = random.randint(-5, 5)
        c2 = random.randint(-5, 5)
    elif difficulty == 'medium':
        a1 = random.randint(-10, 10)
        b1 = random.randint(-20, 20)
        c1 = random.randint(-20, 20)
        a2 = random.randint(-10, 10)
        b2 = random.randint(-20, 20)
        c2 = random.randint(-20, 20)
    elif difficulty == 'hard':
        a1 = random.randint(-20, 20)
        b1 = random.randint(-50, 50)
        c1 = random.randint(-50, 50)
        a2 = random.randint(-20, 20)
        b2 = random.randint(-50, 50)
        c2 = random.randint(-50, 50)

    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    return A, B
