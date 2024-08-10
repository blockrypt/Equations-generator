import random

def generate_quadratic_equation():
    """Генерирует квадратное уравнение вида ax^2 + bx + c = 0 с ограниченными коэффициентами и возвращает коэффициенты a, b и c."""
    a = random.randint(-5, 5)
    while a == 0:
        a = random.randint(-5, 5)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c
